# 📄 PDF Question Answering using Retrieval-Augmented Generation (RAG)

## Overview

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** application that enables users to ask natural language questions from PDF documents.

The application extracts text from a PDF, converts the content into semantic embeddings using Sentence Transformers, stores the embeddings in a FAISS vector database, retrieves the most relevant chunks based on the user's query, and generates accurate answers using **Azure OpenAI GPT-4.1 Mini**.

The project is deployed using **Docker** and provides both:

- FastAPI REST API
- Gradio Web Interface

---

## Features

- 📄 PDF Text Extraction
- ✂ Intelligent Text Chunking
- 🔍 Semantic Search using FAISS
- 🤖 SentenceTransformer Embeddings
- 💬 Azure OpenAI GPT-4.1 Mini Integration
- 🌐 FastAPI REST API
- 🖥 Gradio User Interface
- 🐳 Docker Containerization

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Azure OpenAI | Large Language Model |
| Sentence Transformers | Text Embeddings |
| FAISS | Vector Database |
| FastAPI | REST API |
| Gradio | Web Interface |
| Docker | Containerization |
| PyPDF | PDF Parsing |
| NumPy | Numerical Operations |

---

## Architecture

```
                 PDF Document
                      │
                      ▼
             PDF Text Extraction
                      │
                      ▼
               Text Chunking
                      │
                      ▼
        SentenceTransformer Embeddings
                      │
                      ▼
               FAISS Vector Store
                      │
          User Question
                      │
                      ▼
         Semantic Similarity Search
                      │
                      ▼
         Relevant Context Retrieved
                      │
                      ▼
          Azure OpenAI GPT-4.1 Mini
                      │
                      ▼
                Final Answer
```

---

## Project Structure

```
pdf-rag-chatbot/

│── rag_app.py
│── Dockerfile
│── requirements.txt
│── README.md
│── sample.pdf
│── screenshots/
│── architecture/
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/pdf-rag-chatbot.git

cd pdf-rag-chatbot
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Local

```bash
python rag_app.py
```

---

### Docker

Build Docker Image

```bash
docker build -t pdf-rag .
```

Run Container

```bash
docker run \
-e AZURE_OPENAI_API_KEY=YOUR_KEY \
-p 8000:8000 \
pdf-rag
```

---

## API Endpoint

### Home

```
GET /
```

Returns

```json
{
    "message": "PDF RAG API Running"
}
```

---

### Ask Question

```
POST /ask
```

Example

```
What are the 12 Rules for Life?
```

---

## Future Improvements

- Multiple PDF Upload
- Persistent FAISS Index
- Azure Blob Storage Integration
- Authentication & Authorization
- Streaming Responses
- Chat History
- LangChain Integration

---

## Author

**Gift David**

GitHub:
https://github.com/gift9481780467-lab

LinkedIn:
(Add your LinkedIn URL here)
