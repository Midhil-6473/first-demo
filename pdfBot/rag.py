from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from memory import update_memory, get_history
# from duckduckgo_search import DDGS
from ddgs import DDGS 

def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks

loader = PyPDFLoader("D:\langchain_ai\Data Mining.pdf")
docs = loader.load()

full_text = "\n".join(doc.page_content for doc in docs)
chunks = split_text(full_text)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

vectorstore = FAISS.from_texts(chunks,embeddings)

retriever = vectorstore.as_retriever(search_kws={"k":5})

llm = OllamaLLM(
    model = "llama3.2",
    temperature = 0.8
)

def get_context(query):
    docs = retriever.invoke(query)

    context = "\n\n".join(d.page_content for d in docs)

    return context

#------------------------------------- only for pdfbot-----------------------------------------

# def generate_answer(query, history):
#     context, sources = get_context_and_sources(query)

#     prompt = f"""
# You are a helpful assistant.

# Use ONLY the context below.
# If answer is not present, say "Not found in document."

# Context:
# {context}

# Conversation:
# {history}

# Question:
# {query}
# """

#     response = llm.invoke(prompt)

#     return response, sources

#----------------------------------------------------- tools ----------------------------------------------------

def calculator(args):
    query = args.get("query","")
    try:
        return str(eval(query))
    except:
        return "Invalid math expression"
    
def search_pdf(args: str)-> str:
        query = args.get("query","")
        answer , sources = get_context(query)
        return answer + "\n\nSources:\n" + sources
          
def code(args):
    query = args.get("query","")
    c = llm.invoke(f"write code in the : {query}")
    return c

def email_writer(args: str) -> str:
    query = args.get("query","")
    g = llm.invoke(f"write a professional email for the: {query}")     
    return g  
   

def web_search(args: str) -> str:
    query = args.get("query", "")

    if not query:
        return "No query provided"

    from ddgs import DDGS

    results = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=5):
                results.append(r.get("body", ""))
    except:
        return "Search failed"

    if not results:
        return "No reliable results found"

    return "\n\n".join(results)



# def decide_tool(query):
#     prompt = f"""
# You are an intelligent router.

# Choose the best tool:

# - CALCULATOR → math expressions
# - PDF → questions about documents
# - CODE → programming/code generation
# - MAIL → writing emails/messages
# - WEB -> search web and gather information based on query.latest info / general knowledge / current events

# Rules:
# - Return ONLY one word
# - No explanation

# Query: {query}
# """

#     return llm.invoke(prompt).strip().upper()


tools = {
    "CALCULATOR": calculator,
    "PDF": search_pdf,
    "CODE": code,
    "MAIL": email_writer,
    "WEB": web_search
}


# def agent(query):
#     history = get_history()

#     tool_name = decide_tool(query)

#     tool_output = tools.get(tool_name, lambda x: "Unknown task")(query)


#     final_prompt = f"""
# You are a helpful assistant.

# User question:
# {query}

# Tool result:
# {tool_output}

# Conversation history:
# {history}

# Give a clean, natural final answer.
# """

#     final_answer = llm.invoke(final_prompt)

#     update_memory(query, final_answer)

#     return final_answer


def create_plan(query):
    prompt = f"""
You are an AI planner.

Available tools:
- WEB → search internet
- PDF → document search
- CODE → programming
- CALCULATOR → math
- MAIL → ONLY for writing emails

STRICT RULES:
- DO NOT use MAIL for summarization
- Summarization is done by LLM (no tool needed)
- Use minimum tools
- Max 2 steps

Examples:

Query: latest AI news
Plan:
Step 1: WEB - latest AI news

Query: latest AI news and summarize
Plan:
Step 1: WEB - latest AI news

Query: write email for leave
Plan:
Step 1: MAIL - leave email

Query: 45 * 12
Plan:
Step 1: CALCULATOR - 45 * 12

Query: {query}
"""
    return llm.invoke(prompt)



def parse_plan(plan_text):
    steps = []

    for line in plan_text.split("\n"):
        if "Step" in line and "-" in line:
            parts = line.split("-")
            tool = parts[0].split(":")[1].strip()
            task = parts[1].strip()

            steps.append((tool, task))

    return steps


def execute_plan(steps):
    results = []

    for tool_name, task in steps:
        tool_func = tools.get(tool_name)

        if not tool_func:
            results.append(f"{tool_name}: Tool not found")
            continue

        try:
            output = tool_func({"query": task})

            if not output or len(output.strip()) < 20:
                output = "Low quality result"

            results.append(f"{tool_name}: {output}")

        except Exception as e:
            results.append(f"{tool_name}: Error - {str(e)}")

    return "\n\n".join(results)




def autonomous_agent(query):
    history = get_history()

    plan = create_plan(query)
    print("\nPLAN:\n", plan)

    if "NO_TOOL" in plan:
        final_answer = llm.invoke(query)
        update_memory(query, final_answer)
        return final_answer

    steps = parse_plan(plan)

    results = execute_plan(steps)

    final_prompt = f"""
You are a helpful assistant.

Use ONLY the tool results below.

User query:
{query}

Tool results:
{results}

Give a clear answer.
"""

    final_answer = llm.invoke(final_prompt)

    update_memory(query, final_answer)

    return final_answer

