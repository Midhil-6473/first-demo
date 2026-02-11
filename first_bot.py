import os
import streamlit as st
from langchain_community.llms import Ollama 
from langchain_ollama import OllamaLLM,OllamaEmbeddings
from langchain_core.prompts import PromptTemplate,ChatPromptTemplate
from langchain_core.tools import tool
from langchain_core.runnables import RunnablePassthrough
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS


# ------------------------------------------------- basic usage -------------------------------------------------
# llm = Ollama (
#     model = "llama3.2",
#     temperature = 0.7
# )

# response = llm.invoke("What is Archlinux and how to install it in steps using virtualbox?")
# print(response)

# ------------------------------------------------- prompt template usage -------------------------------------------------

# llm = Ollama(
#     model="llama3.2",
#     temperature=0.3
# )

# prompt = PromptTemplate (
#     input_variables=["topic"],
#     template="Explain {topic} in simple words for a 10 year old."
# )

# formatted = prompt.format(topic = "Machine Learning")

# response = llm.invoke(formatted)
# print(response)

#----------------------------------------------------------------- memory usage -------------------------------------------------
# llm = Ollama (
#     model = "llama3.2",
#     temperature = 0.8
# )

# memory = ConversationBufferMemory()

# chat = ConversationChain(
#     llm=llm,
#     memory=memory
# )

# print(chat.predict(input="Hello"))
# print(chat.predict(input="What is my previous message?"))

# ------------------------------------------------- chain -------------------------------------------------

# llm = Ollama (
#     model = "llama3.2",
#     temperature = 0.8
# )

# prompt = PromptTemplate(
#     input_variables = ["topic"],
#     template = "Explain {topic} like I am 10 years old."
# )

# chain = prompt | llm

# response = chain.invoke({"topic": "Quantum Computing"})
# print(response)

# ------------------------------------------------- tool usage -------------------------------------------------

# @tool
# def multiply(a: int,b: int) -> int:
#     """Multiply two numbers a and b."""
#     return a*b

# def add(a: int,b: int) -> int:
#     """Add two numbers a and b."""
#     return a+b

# def subtract(a: int,b: int) -> int:
#     """Subtract two numbers a and b."""
#     return a-b

# def divide(a: int,b: int) -> float:
#     """Divide two numbers a and b."""
#     return a/b

# def explain(topic: str) -> str:
#     f"""Explain a {topic} in simple words for a 10 year old in points."""
#     return topic

# tools = [multiply, add, subtract, divide, explain]

# llm = ChatGoogleGenerativeAI(
#     model = "gemini-2.5-flash",
#     temperature = 0.7
# )

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "you are an AI assitant to use the tools to answer the questions, when needed use the tools."),
#     ("human","{input}")
# ])

# bind_tool = llm.bind_tools(tools)

# chain = (
#     {"input": RunnablePassthrough()} 
#     | prompt
#     | bind_tool
# )

# response = chain.invoke({"input": "Add 234 and 76343"})
# print(response.content)

# ------------------------------------------------- custom ollama llm usage -------------------------------------------------

# llm = OllamaLLM (
#     model = "llama3.2",
#     temperature = 0.7
# )

# memory = ConversationBufferMemory(return_messages=True)

# prompt = ChatPromptTemplate.from_messages([
#     ("system", "You are a helpful assistant that helps users with their queries."),
#     ("history", "{history}"),
#     ("human", "{input}")
# ])

# def load_history():
#     return memory.load_memory_variables({})["history"]

# chain = ({
#     "input": RunnablePassthrough(),
#     "history": load_history
#     }
#     | prompt
#     | llm
# )

# con = input()

# while True:
#     if con == "exit":
#         break
#     user_input = input("User: ")
#     response = chain.invoke({"input": user_input})
#     print("Bot:", response)
#     memory.save_context({"input": user_input}, {"output": response})

#------------------------------------------------- memory chatbot -------------------------------------------------

# from langchain_ollama import OllamaLLM

# llm = OllamaLLM(
#     model="llama3.2",
#     temperature=0.3
# )
# chat_history = []

# print("Chatbot with memory (type exit to stop)\n")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

#     history_text = "\n".join(chat_history)

#     prompt = f"""
# You are a helpful AI assistant.

# Conversation so far:
# {history_text}

# User: {user_input}
# AI:
# """

#     response = llm.invoke(prompt)

#     print("AI:", response)

#     chat_history.append(f"User: {user_input}")
#     chat_history.append(f"AI: {response}")

#------------------------------------------------- document chatbot -------------------------------------------------

# def split_text(text, chunk_size=500, overlap=100):
#     chunks = []
#     start = 0

#     while start < len(text):
#         end = start + chunk_size
#         chunk = text[start:end]
#         chunks.append(chunk)
#         start = end - overlap

#     return chunks

# loader_pdf = PyPDFLoader("data/[7] Component Based Model (CBM).pdf")
# documents = loader_pdf.load()

# full_text = "\n".join([doc.page_content for doc in documents])

# chunks = split_text(full_text)

# docs = [{"page_content": c} for c in chunks]

# embeddings = OllamaEmbeddings(model="nomic-embed-text")

# vectorstore = FAISS.from_texts(chunks, embeddings)

# # LLM
# llm = OllamaLLM(model="llama3.2")

# print("PDF chatbot ready\n")

# while True:
#     query = input("Ask PDF: ")
#     if query.lower() == "exit":
#         break

#     results = vectorstore.similarity_search(query, k=3)
#     context = "\n\n".join([r.page_content for r in results])

#     prompt = f"""
#     Answer ONLY from the context below.

#     Context:
#     {context}

#     Question:
#     {query}
#     """

#     answer = llm.invoke(prompt)
#     print("AI:", answer)

#---------------------------------------------------------------- memory based pdf reader chatbot -------------------------------------------------

# def split_text(text, chunk_size=500, overlap=100):
#     chunks = []
#     start = 0

#     while start < len(text):
#         end = start + chunk_size
#         chunk = text[start:end]
#         chunks.append(chunk)
#         start = end - overlap

#     return chunks

# loader_pdf = PyPDFLoader("data/[7] Component Based Model (CBM).pdf")
# documents = loader_pdf.load()

# full_text = "\n".join([doc.page_content for doc in documents])

# chunks = split_text(full_text)

# docs = [{"page_content":c} for c in chunks]

# embeddings = OllamaEmbeddings(model = "nomic-embed-text")

# vectorstore = FAISS.from_texts(chunks, embeddings)

# llm = OllamaLLM(model = "llama3.2")

# chat_history = []

# while True:
#     query = input("Ask Question: ")
#     if query.lower() == "exit":
#         break
    
#     n = int(input("Number of context chunks to use (e.g., 5): "))

#     results = vectorstore.similarity_search(query,k = n)
#     context = "\n\n".join([r.page_content for r in results])
#     history_text = "\n".join(chat_history)
#     prompt = f"""
#     you are an AI assitant to answer and summarize the user's questions based on the context and prevoious chat history.
#     context:
#     {context}
#     history:
#     {history_text}

#     question:
#     {query}
#     """
#     response = llm.invoke(prompt)
#     print("AI: ",response)

#     chat_history.append(f"User: {query}")
#     chat_history.append(f"AI: {response}")

#------------------------------------------------- multiple pdfs -------------------------------------------------
# def split_text(text, chunk_size=500, overlap=100):
#     chunks = []
#     start = 0

#     while start < len(text):
#         end = start + chunk_size
#         chunk = text[start:end]
#         chunks.append(chunk)
#         start = end - overlap

#     return chunks

# full_text = ""

# for file in os.listdir("data"):
#     if file.endswith(".pdf"):
#         load_pdf = PyPDFLoader(f"data/{file}")
#         document = load_pdf.load()
#         full_text += "\n".join([doc.page_content for doc in document])

# chunks = split_text(full_text)

# docs = [{"page_content":c} for c in chunks]

# embeddings = OllamaEmbeddings(model = "nomic-embed-text")

# vectorstore = FAISS.from_texts(chunks, embeddings)

# llm = OllamaLLM(model = "llama3.2")

# chat_history = []

# while True:
#     query = input("Ask Question: ")
#     if query.lower() == "exit":
#         break

#     n = int(input("Number of context chunks to use (e.g., 5): "))
#     results = vectorstore.similarity_search(query, k = n)
#     context = "\n\n".join([r.page_content for r in results])
#     history_chat = "\n".join(chat_history)
#     prompt = f"""
#     you are an AI assitant to answer and summarize User's pdf and answer the questions based on the context on the pdf and prevoius chat history.
#     history:
#     {history_chat}
#     Context:
#     {context}

#     Question:
#     {query}
#     """
#     response = llm.invoke(prompt)
#     print("AI: ", response)

#     chat_history.append(f"User: {query}")
#     chat_history.append(f"AI: {response}")

#------------------------------------------------- streamlit app -------------------------------------------------      
# import streamlit as st
# from langchain_ollama import OllamaLLM, OllamaEmbeddings
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.vectorstores import FAISS

# # -----------------------------
# # Text splitter
# # -----------------------------
# def split_text(text, chunk_size=500, overlap=100):
#     chunks = []
#     start = 0
#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start = end - overlap
#     return chunks

# # -----------------------------
# # Page config
# # -----------------------------
# st.set_page_config(page_title="PDF Chatbot", layout="centered")
# st.title("📘 PDF Chatbot")

# # -----------------------------
# # Load once
# # -----------------------------
# @st.cache_resource
# def load_pdf():
#     loader = PyPDFLoader("data/[7] Component Based Model (CBM).pdf")
#     docs = loader.load()

#     full_text = "\n".join([d.page_content for d in docs])
#     chunks = split_text(full_text)

#     embeddings = OllamaEmbeddings(model="nomic-embed-text")
#     vectorstore = FAISS.from_texts(chunks, embeddings)

#     return vectorstore

# vectorstore = load_pdf()

# llm = OllamaLLM(model="llama3.2", temperature=0)

# # -----------------------------
# # Session memory
# # -----------------------------
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # -----------------------------
# # Display history
# # -----------------------------
# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# # -----------------------------
# # Input
# # -----------------------------
# user_input = st.chat_input("Ask from PDF...")

# if user_input:
#     # show user message
#     st.session_state.messages.append(
#         {"role": "user", "content": user_input}
#     )

#     with st.chat_message("user"):
#         st.markdown(user_input)

#     # retrieve context
#     docs = vectorstore.similarity_search(user_input, k=3)
#     context = "\n\n".join([d.page_content for d in docs])

#     prompt = f"""
# Answer ONLY from the context below.

# Context:
# {context}

# Question:
# {user_input}
# """

#     response = llm.invoke(prompt)

#     # show AI response
#     with st.chat_message("assistant"):
#         st.markdown(response)

#     st.session_state.messages.append(
#         {"role": "assistant", "content": response}
#     )
 
import streamlit as st
from langchain_ollama import OllamaLLM, OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
import tempfile
import os


# def split_text(text, chunk_size=500, overlap=100):
#     chunks = []
#     start = 0
#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start = end - overlap
#     return chunks


# st.set_page_config(page_title="PDF Chatbot", layout="centered")
# st.title("📘 Chat with your PDF")


# if "vectorstore" not in st.session_state:
#     st.session_state.vectorstore = None

# if "messages" not in st.session_state:
#     st.session_state.messages = []


# uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

# if uploaded_file:
#     with st.spinner("Processing PDF..."):


#         with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
#             tmp.write(uploaded_file.read())
#             temp_path = tmp.name


#         loader = PyPDFLoader(temp_path)
#         documents = loader.load()

#         full_text = "\n".join([d.page_content for d in documents])
#         chunks = split_text(full_text)

#         embeddings = OllamaEmbeddings(model="nomic-embed-text")
#         st.session_state.vectorstore = FAISS.from_texts(chunks, embeddings)

#         os.remove(temp_path)

#         st.success("PDF loaded successfully!")


# if st.session_state.vectorstore:

#     llm = OllamaLLM(model="llama3.2", temperature=0)

#     for msg in st.session_state.messages:
#         with st.chat_message(msg["role"]):
#             st.markdown(msg["content"])

#     user_input = st.chat_input("Ask something from the PDF...")

#     if user_input:

#         st.session_state.messages.append(
#             {"role": "user", "content": user_input}
#         )

#         with st.chat_message("user"):
#             st.markdown(user_input)

#         docs = st.session_state.vectorstore.similarity_search(user_input, k=3)
#         context = "\n\n".join([d.page_content for d in docs])

#         prompt = f"""
# You are a helpful study assistant.

# Rules:
# - Use ONLY the provided context.
# - Do NOT use outside knowledge.
# - If the answer is not in the context, say:
#   "Not found in the document."

# Explain clearly in simple words.

# Context:
# {context}

# Question:
# {user_input}
# """


#         response = llm.invoke(prompt)

#         with st.chat_message("assistant"):
#             st.markdown(response)

#         st.session_state.messages.append(
#             {"role": "assistant", "content": response}
#         )

# import re

# llm = OllamaLLM(
#     model = "llama3.2",
#     temperature = 0.8
# )

# def decision_maker(user_input: str) -> str:
#     prompt = f"""
# You are a router.

# Decide what action is needed.

# Actions:
# - CALCULATE (math)
# - SEARCH_PDF (questions about document)
# - CHAT (normal conversation)

# Respond with ONLY ONE WORD.

# User query:
# {user_input}
# """
#     return llm.invoke(prompt).strip()


# def calculate(text: str) -> str:
#     try:
#         expression = "".join(re.findall(r"[0-9+\-*/().]", text))
#         return str(eval(expression))
#     except Exception:
#         return "Invalid calculation"

# def chat(text: str) -> str:
#     return llm.invoke(text) 

# def split_text(text, chunk_size=500, overlap=100):
#     chunks = []
#     start = 0
#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start = end - overlap
#     return chunks   

# load_pdf = PyPDFLoader("Data mining.pdf")
# documents = load_pdf.load()

# full_text = "\n".join([d.page_content for d in documents])
# chunks = split_text(full_text)

# embeddings = OllamaEmbeddings(model="nomic-embed-text")
# vectorstore = FAISS.from_texts(chunks,embeddings)    

# def search_pdf(query: str) -> str:
#     docs = vectorstore.similarity_search(query, k=5)
#     if not docs:
#         return "No relevant information found in the document."
#     return "\n\n".join([d.page_content for d in docs])

# def agent(user_input: str) -> str:
#     decision = decision_maker(user_input)

#     if decision.lower() == "calculate":
#         return calculate(user_input)
#     elif decision.lower() == "search_pdf":
#         context = search_pdf(user_input)
#         prompt = f"""
# Answer ONLY using the context below.
# If not found, say: Not found in the document.

# Context:
# {context}

# Question:
# {user_input}
# """
#         return llm.invoke(prompt)
#     else:
#         return chat(user_input)
    
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Goodbye!")
#         break
#     response = agent("AI: " + user_input)
#     print(response)


# def split_text(text, chunk_size=500, overlap=100):
#     chunks = []
#     start = 0
#     while start < len(text):
#         end = start + chunk_size
#         chunks.append(text[start:end])
#         start = end - overlap
#     return chunks   

# load_pdf = PyPDFLoader("Data mining.pdf")
# documents = load_pdf.load()

# full_text = "\n".join([d.page_content for d in documents])
# chunks = split_text(full_text)

# embeddings = OllamaEmbeddings(model="nomic-embed-text")
# vectorstore = FAISS.from_texts(chunks,embeddings) 

# retriever = vectorstore.as_retriever(search_kwargs = {"k": 5})

# prompt = ChatPromptTemplate.from_messages([
#     ("system", 
#      "You are a helpful assistant. "
#      "Answer ONLY using the provided context. "
#      "If the answer is not in the context, say 'Not found in the document.'"),
#     ("human", "{question}")
# ])

# llm = OllamaLLM(model="llama3.2", temperature=0.5)

# chain = ({
#     "context":retriever,
#     "question":RunnablePassthrough()
#     | prompt
#     | llm
# })

# while True:
#     user_input = input("you: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Goodbye!")
#         break
#     response = chain["question"].invoke(user_input)
#     print("AI:", response)

from langchain_core.messages import HumanMessage, AIMessage

def split_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks   

load_pdf = PyPDFLoader("Data mining.pdf")
documents = load_pdf.load()

full_text = "\n".join([d.page_content for d in documents])
chunks = split_text(full_text)

embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = FAISS.from_texts(chunks,embeddings) 

retriever = vectorstore.as_retriever(search_kwargs = {"k": 5})

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You are a helpful assistant. "
     "Answer ONLY using the provided context. "
     "If the answer is not in the context, say 'Not found in the document.'"),
    ("human", "{question}")
])

llm = OllamaLLM(model="llama3.2", temperature=0.5)

history = []
chain = ({
    "context":retriever,
    "question":RunnablePassthrough(),
    "history":RunnablePassthrough()
    | prompt
    | llm
})

def ask(question: str) -> str:
    global history
    message = history + [HumanMessage(content=question)]   
    response = llm.invoke(message)
    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=response.content))
    return response.content

ask("What is data mining?")

# while True:
#     user_input = input("you: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Goodbye!")
#         break
#     response = chain["question"].invoke(user_input)
#     print("AI:", response)