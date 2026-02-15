from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS



def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap

    return chunks

loader = PyPDFLoader("Data Mining.pdf")
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


def generate_answer(query, history):
    context, sources = get_context_and_sources(query)

    prompt = f"""
You are a helpful assistant.

Use ONLY the context below.
If answer is not present, say "Not found in document."

Context:
{context}

Conversation:
{history}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response, sources