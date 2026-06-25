# Fix sqlite3 issue on Streamlit Cloud
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate

# FIXED: Explicitly added the missing Google GenAI imports
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI 

# FIXED: Unified and cleaned up the conflicting chain imports
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain

# 1. Handle API Keys gracefully whether running locally or on Streamlit Cloud
try:
    secrets = st.secrets
except FileNotFoundError:
    secrets = {}

if "GOOGLE_API_KEY" in secrets:
    os.environ["GOOGLE_API_KEY"] = secrets["GOOGLE_API_KEY"]
elif os.environ.get("GOOGLE_API_KEY"):
    pass
else:
    st.error("Missing Google API Key! Please set it in Streamlit Secrets or environment variables.")
    st.stop()

st.set_page_config(page_title="Cloud RAG Chatbot", layout="wide")
st.title("🚀 Production Cloud RAG Chatbot")
st.write("Upload a PDF to test this live portfolio application.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

with st.sidebar:
    st.header("Document Ingestion")
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")
    
    if uploaded_file is not None:
        with st.spinner("Processing document..."):
            temp_file_path = f"temp_{uploaded_file.name}"
            with open(temp_file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            try:
                loader = PyPDFLoader(temp_file_path)
                docs = loader.load()
                
                text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
                final_documents = text_splitter.split_documents(docs)
                
                embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
                st.session_state.vector_store = Chroma.from_documents(
                    final_documents, embeddings, collection_name="cloud_pdf_base"
                )
                st.success("Document indexed! Ready to chat.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
            finally:
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

if st.session_state.vector_store is None:
    st.info("Please upload a PDF document in the sidebar to activate the chatbot.")
else:
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    if user_query := st.chat_input("Ask a question about your document:"):
        with st.chat_message("user"):
            st.markdown(user_query)
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        
        retriever = st.session_state.vector_store.as_retriever(search_kwargs={"k": 3})
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        system_prompt = (
            "You are an expert assistant answering questions based strictly on the provided context.\n"
            "If you do not know the answer based on the context, say that you cannot find the answer.\n\n"
            "Context:\n{context}"
        )
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{input}"),
        ])
        
        question_answer_chain = create_stuff_documents_chain(llm, prompt)
        rag_chain = create_retrieval_chain(retriever, question_answer_chain)
        
        with st.chat_message("assistant"):
            with st.spinner("Generating answer via Gemini API..."):
                response = rag_chain.invoke({"input": user_query})
                answer = response["answer"]
                st.markdown(answer)
                        
        st.session_state.chat_history.append({"role": "assistant", "content": answer})
