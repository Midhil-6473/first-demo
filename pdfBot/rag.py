from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from memory import update_memory, get_history


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

def get_context_and_sources(query):
    docs = retriever.invoke(query)

    context = "\n\n".join(d.page_content for d in docs)

    sources = "\n\n".join(
        f"[Source {i+1}]\n{d.page_content[:200]}..."
        for i, d in enumerate(docs)
    )

    return context, sources

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

def calculator(query):
    try:
        return str(eval(query))
    except:
        return "Invalid math expression"
    
def search_pdf(query):
    history =  get_history()
    answer , sources = get_context_and_sources(query,history)
    return answer + "\n\nSources:\n" + sources
          
def code(query):
    c = llm.invoke(f"write code in the : {query}")
    return c

def email_writer(query):
    g = llm.invoke(f"write a professional email for the: {query}")     
    return g     


def decide_tool(query):
    prompt = f"""
You are an intelligent router.

Choose the best tool:

- CALCULATOR → math expressions
- PDF → questions about documents
- CODE → programming/code generation
- MAIL → writing emails/messages

Rules:
- Return ONLY one word
- No explanation

Query: {query}
"""

    return llm.invoke(prompt).strip().upper()


tools = {
    "CALCULATOR": calculator,
    "PDF": search_pdf,
    "CODE": code,
    "MAIL": email_writer
}


def agent(query):
    history = get_history()

    tool_name = decide_tool(query)

    tool_output = tools.get(tool_name, lambda x: "Unknown task")(query)


    final_prompt = f"""
You are a helpful assistant.

User question:
{query}

Tool result:
{tool_output}

Conversation history:
{history}

Give a clean, natural final answer.
"""

    final_answer = llm.invoke(final_prompt)

    update_memory(query, final_answer)

    return final_answer