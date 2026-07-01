# 📄 PDF Question Answering using Retrieval-Augmented Generation (RAG)

## Overview

This project is an end-to-end **Retrieval-Augmented Generation (RAG)** application that enables users to ask natural language questions from PDF documents.

The application extracts text from a PDF, converts the content into semantic embeddings using Sentence Transformers, stores the embeddings in a FAISS vector database, retrieves the most relevant chunks based on the user's query, and generates accurate answers using **Azure OpenAI GPT-4.1 Mini**.

The project is containerized using **Docker** and provides both:

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
- 🖥️ Gradio User Interface
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

```text
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

```text
PDF_QA_RAG/

│── rag_app.py
│── pdf_qa.py
│── Dockerfile
│── requirements.txt
│── README.md
│── 12 Rules for Life An Antidote to Chaos (PDF)
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/gift9481780467-lab/PDF_QA_RAG.git

cd PDF_QA_RAG
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

### Run Locally

```bash
python rag_app.py
```

---

### Run with Docker

Build the Docker image

```bash
docker build -t pdf-rag .
```

Run the Docker container

```bash
docker run -e AZURE_OPENAI_API_KEY=YOUR_KEY -p 8000:8000 pdf-rag
```

---

## API Endpoints

### Home

```
GET /
```

Response

```json
{
  "message": "PDF RAG API Running"
}
```

---

### Ask a Question

```
POST /ask
```

Example Question

```
What are the 12 Rules for Life?
```

---

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Azure OpenAI Integration
- Semantic Search
- Vector Databases (FAISS)
- Sentence Transformers
- FastAPI
- Docker
- REST API Development
- Natural Language Processing (NLP)
- Prompt Engineering

---

## Future Improvements

- Support multiple PDF uploads
- Persistent FAISS vector database
- Azure Blob Storage integration
- User Authentication
- Streaming responses
- Chat history
- LangChain integration

---

## Screenshots

> Screenshots of the Gradio interface and Docker deployment will be added soon.

---

## Author

**Gift David**

- GitHub: https://github.com/gift9481780467-lab
- LinkedIn: *(Add your LinkedIn profile URL here)*

---

## License

This project is intended for learning and portfolio purposes.
