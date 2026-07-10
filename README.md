# 🤖 RAG-Based Chatbot using OpenAI, FAISS & FastAPI

A Retrieval-Augmented Generation (RAG) chatbot that answers user queries by retrieving relevant information from custom documents instead of relying only on the LLM's pretrained knowledge.

The application uses **OpenAI Embeddings**, **FAISS Vector Database**, and **FastAPI** to provide accurate, context-aware responses with low latency.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- ✂️ Intelligent document chunking
- 🧠 Generate embeddings using OpenAI
- 🔍 Fast semantic search using FAISS
- 💬 Context-aware chatbot responses
- ⚡ REST API built with FastAPI
- 🔄 Retrieval-Augmented Generation (RAG)
- 📚 Handles multiple documents
- 📝 Source-based answer generation
- 🔐 Environment variable support

---

## 🏗️ Architecture

```
                    User Query
                         │
                         ▼
                  FastAPI Endpoint
                         │
                         ▼
              Generate Query Embedding
                         │
                         ▼
              Search FAISS Vector Store
                         │
         Top-K Relevant Document Chunks
                         │
                         ▼
      Build Prompt (Context + User Question)
                         │
                         ▼
                  OpenAI GPT Model
                         │
                         ▼
                  Generated Response
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| FastAPI | REST API |
