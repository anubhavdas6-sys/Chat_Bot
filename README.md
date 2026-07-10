# 🤖 RAG-Based PDF Chatbot using Gemini 1.5 Flash & ChromaDB

A **Retrieval-Augmented Generation (RAG)** chatbot that enables users to ask questions about PDF documents using natural language. The application leverages **Google Gemini 1.5 Flash**, **Google Generative AI Embeddings**, and **ChromaDB** to retrieve relevant document content and generate accurate, context-aware answers.

This project demonstrates a complete RAG pipeline, including document ingestion, text chunking, embedding generation, vector storage, semantic retrieval, and response generation.

---

## 🚀 Features

- 📄 Upload and process one or more PDF documents
- ✂️ Intelligent text chunking for improved retrieval
- 🧠 Generate embeddings using Google Generative AI Embeddings
- 🔍 Store and retrieve document vectors with ChromaDB
- 💬 Context-aware question answering using Gemini 1.5 Flash
- ⚡ Fast and lightweight RAG pipeline
- 📚 Multi-document support
- 🔐 Environment variable configuration
- 🏗️ Modular and scalable project structure

---

## 🏗️ System Architecture

```
                     User Question
                           │
                           ▼
                    Query Embedding
                           │
                           ▼
                ChromaDB Vector Search
                           │
          Top-K Relevant Document Chunks
                           │
                           ▼
        Prompt (Context + User Question)
                           │
                           ▼
              Gemini 1.5 Flash LLM
                           │
                           ▼
                  Generated Answer
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Google Gemini 1.5 Flash | Large Language Model |
| Google Generative AI Embeddings | Text Embeddings |
| ChromaDB | Vector Database |
| LangChain | RAG Framework |
| PyPDF2 / PyMuPDF | PDF Processing |
| Streamlit / FastAPI *(Optional)* | User Interface / API |
| python-dotenv | Environment Variables |

---

## 📂 Project Structure

```
rag-pdf-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .env
│
├── data/
│   └── sample.pdf
│
├── chroma_db/
│
├── utils/
│   ├── pdf_loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── chatbot.py
│
└── assets/
```

> *The folder structure may vary depending on your implementation.*

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-pdf-chatbot.git

cd rag-pdf-chatbot
```

---

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv

venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_api_key
```

---

## ▶️ Running the Application

If using **Streamlit**:

```bash
streamlit run app.py
```

If using **FastAPI**:

```bash
uvicorn app:app --reload
```

---

## 📖 How It Works

### Step 1: Document Upload

The chatbot loads one or more PDF documents.

↓

### Step 2: Text Extraction

Text is extracted from each PDF page.

↓

### Step 3: Chunking

The extracted text is divided into overlapping chunks for better semantic retrieval.

↓

### Step 4: Embedding Generation

Each chunk is converted into vector embeddings using **Google Generative AI Embeddings**.

↓

### Step 5: Vector Storage

Embeddings are stored in **ChromaDB** for efficient similarity search.

↓

### Step 6: User Query

The user's question is embedded using the same embedding model.

↓

### Step 7: Retrieval

The most relevant document chunks are retrieved from ChromaDB.

↓

### Step 8: Answer Generation

Retrieved context and the user's question are sent to **Gemini 1.5 Flash**, which generates a grounded, context-aware response.

---

## 🔄 RAG Workflow

```
PDF Documents
      │
      ▼
Text Extraction
      │
      ▼
Text Chunking
      │
      ▼
Google Embeddings
      │
      ▼
ChromaDB
      │
      ▼
User Question
      │
      ▼
Query Embedding
      │
      ▼
Similarity Search
      │
      ▼
Relevant Context
      │
      ▼
Gemini 1.5 Flash
      │
      ▼
Generated Response
```

---

## 📌 Example Usage

**User Question**

```
What are the eligibility criteria mentioned in the document?
```

**Chatbot Response**

```
According to the uploaded PDF, the eligibility criteria include:

• Bachelor's degree in Computer Science or related field.
• Minimum 2 years of professional experience.
• Strong knowledge of Python and REST APIs.

These requirements are listed in Section 3 of the document.
```

---

## 🎯 Advantages

- Accurate responses grounded in uploaded documents
- Reduces hallucinations by providing document context
- Supports semantic search across large PDFs
- Fast retrieval with ChromaDB
- Easy to extend for enterprise knowledge bases
- Modular and reusable architecture

---

## 🔮 Future Enhancements

- Chat history and conversational memory
- Source citations with page numbers
- Hybrid search (Keyword + Vector Search)
- Metadata filtering
- OCR support for scanned PDFs
- Multiple document collections
- Authentication and user management
- Docker deployment
- Cloud storage integration
- Streaming responses
- Feedback and evaluation metrics

---

## 📦 Requirements

```
Python 3.10+

langchain
langchain-google-genai
chromadb
google-generativeai
PyPDF2
python-dotenv
streamlit (optional)
fastapi (optional)
uvicorn (optional)
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Anubhav Das**

**AI / GenAI Developer**

### Skills

- Python
- Retrieval-Augmented Generation (RAG)
- Google Gemini
- Google Generative AI Embeddings
- ChromaDB
- LangChain
- FastAPI
- Streamlit
- Prompt Engineering
- Vector Databases
- Large Language Models (LLMs)

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.

It helps others discover the project and motivates future improvements.
