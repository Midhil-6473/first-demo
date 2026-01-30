import streamlit as st
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
import tempfile
import os


def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks


st.set_page_config(page_title="PDF Chatbot", layout="centered")
st.title("📘 Chat with your PDF")


if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "messages" not in st.session_state:
    st.session_state.messages = []


uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):


        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            temp_path = tmp.name


        loader = PyPDFLoader(temp_path)
        documents = loader.load()

        full_text = "\n".join([d.page_content for d in documents])
        chunks = split_text(full_text)

        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        st.session_state.vectorstore = FAISS.from_texts(chunks, embeddings)

        os.remove(temp_path)

        st.success("PDF loaded successfully!")


if st.session_state.vectorstore:

    llm = OllamaLLM(model="llama3.2", temperature=0)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask something from the PDF...")

    if user_input:

        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("user"):
            st.markdown(user_input)

        docs = st.session_state.vectorstore.similarity_search(user_input, k=3)
        context = "\n\n".join([d.page_content for d in docs])

        prompt = f"""
Answer ONLY from the context below.

Context:
{context}

Question:
{user_input}
"""

        response = llm.invoke(prompt)

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append(
            {"role": "assistant", "content": response}
        )