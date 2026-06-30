# 🚀 DocuTrust Ultra – Enterprise AI Document Assistant

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Enterprise-green?style=for-the-badge&logo=fastapi)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange?style=for-the-badge&logo=google)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-darkgreen?style=for-the-badge&logo=mongodb)
![ChromaDB](https://img.shields.io/badge/Vector-Database-red?style=for-the-badge)
![React](https://img.shields.io/badge/Frontend-React-blue?style=for-the-badge&logo=react)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

## 📌 Overview

**DocuTrust Ultra** is a next-generation AI-powered Enterprise Document Assistant built using **Retrieval-Augmented Generation (RAG)** architecture.

The application enables users to upload PDF documents, automatically extract and index their contents using vector embeddings, and interact with them through natural language conversations powered by **Google Gemini AI**.

Unlike traditional chatbots, DocuTrust Ultra generates responses grounded entirely in uploaded documents, ensuring contextual accuracy, transparency, and reliable source citations.

---

# ✨ Key Features

- 📄 Intelligent PDF Upload
- 📑 Automatic Document Parsing
- ✂️ Smart Text Chunking
- 🧠 Sentence Transformer Embeddings
- 🔍 Semantic Similarity Search
- ⚡ Retrieval-Augmented Generation (RAG)
- 🤖 Google Gemini AI Integration
- 📚 Source Citation Support
- 🗂 Chroma Vector Database
- ☁ MongoDB Atlas Integration
- 🚀 FastAPI REST APIs
- 📖 Swagger API Documentation
- 🔒 Secure Environment Configuration
- ⚙ Modular Enterprise Architecture

---

# 🏗 System Architecture

```
                User
                  │
                  ▼
         Upload PDF Document
                  │
                  ▼
         PDF Parsing (PyMuPDF)
                  │
                  ▼
          Text Chunking Engine
                  │
                  ▼
      SentenceTransformer Embeddings
                  │
                  ▼
          Chroma Vector Database
                  │
                  ▼
         Semantic Similarity Search
                  │
                  ▼
          Relevant Context Retrieval
                  │
                  ▼
            Google Gemini AI
                  │
                  ▼
          AI Generated Response
                  │
                  ▼
     Answer + Source Citations
```

---

# 🧠 AI Workflow

```
Upload PDF

    ↓

Extract Text

    ↓

Split into Chunks

    ↓

Generate Embeddings

    ↓

Store in ChromaDB

    ↓

User asks Question

    ↓

Embedding Generation

    ↓

Similarity Search

    ↓

Retrieve Context

    ↓

Gemini AI

    ↓

Answer with Sources
```

---

# 🛠 Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| Backend | FastAPI |
| AI Model | Google Gemini |
| Embeddings | SentenceTransformers |
| Vector Database | ChromaDB |
| Database | MongoDB Atlas |
| PDF Processing | PyMuPDF |
| API Documentation | Swagger UI |
| Frontend | React / Next.js |
| Version Control | Git & GitHub |
| Deployment | Render & Vercel |

---

# 📂 Project Structure

```
DocuTrustUltra/

│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── database/
│   │   ├── services/
│   │   ├── schemas/
│   │   ├── config/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│
├── README.md
│
└── docker-compose.yml
```

---

# ⚡ REST API

## Upload Document

```
POST /upload
```

Uploads a PDF document for processing and vector indexing.

---

## Ask Questions

```
POST /chat
```

Example Request

```json
{
  "question":"What skills are mentioned?"
}
```

Example Response

```json
{
    "answer":"The document mentions Python, FastAPI and MongoDB.",

    "sources":[
        {
            "document":"Resume.pdf",
            "page":2,
            "chunk":"Python, FastAPI, MongoDB..."
        }
    ]
}
```

---

# 🔍 Retrieval-Augmented Generation (RAG)

The project follows a complete Retrieval-Augmented Generation pipeline:

- Document Parsing
- Intelligent Chunking
- Embedding Generation
- Vector Storage
- Semantic Search
- Context Retrieval
- Prompt Engineering
- Google Gemini Response Generation
- Source Citation

This significantly reduces hallucinations by grounding responses in the uploaded documents.

---

# 📈 Enterprise Highlights

- Modular Architecture
- Scalable Backend
- Clean Code Structure
- API-First Design
- Vector Search
- AI-Powered Search Engine
- Production Ready
- Extensible Design
- Enterprise Documentation

---

# 🔒 Security

- Environment Variables
- Secure API Keys
- MongoDB Atlas Authentication
- Input Validation
- Error Handling
- Modular Configuration

---

# 🚀 Deployment

### Backend

Render

### Frontend

Vercel

### Database

MongoDB Atlas

### Vector Database

ChromaDB

---

# 📊 Future Enhancements

- Multi PDF Workspace
- Authentication
- User Dashboard
- Chat History
- Streaming Responses
- OCR Support
- Multi-language Documents
- Document Versioning
- Citation Highlighting
- Cloud Storage
- Admin Dashboard

---

# 📸 Screenshots

> Add screenshots here after deployment.

- Dashboard
- Upload Page
- Chat Interface
- Swagger API
- Source Citation Results

---

# 👨‍💻 Author

**Anurag Sahu**

AI & Machine Learning Enthusiast

---

# ⭐ Support

If you found this project helpful,

⭐ Star this repository

🍴 Fork it

🛠 Contribute

---

# 📜 License

This project is licensed under the MIT License.

---

## 🌟 DocuTrust Ultra

**Enterprise AI Document Assistant powered by Retrieval-Augmented Generation (RAG), Google Gemini AI, FastAPI, ChromaDB, MongoDB Atlas, and Modern AI Engineering Practices.**
