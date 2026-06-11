from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import gradio as gr
from transformers import pipeline

# Load PDF
pdf = PdfReader(
    "12 Rules for Life An Antidote to Chaos ( PDFDrive.com )-1.pdf"
)

text = ""

for page in pdf.pages:
    page_text = page.extract_text()

    if page_text:
        text += page_text

# Chunking
chunks = []

for i in range(0, len(text), 500):
    chunks.append(text[i:i+500])

# Embeddings
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
generator = pipeline(
    "text-generation",
    model="gpt2"
)

embeddings = model.encode(
    chunks
).astype("float32")

# FAISS
index = faiss.IndexFlatL2(
    embeddings.shape[1]
)

index.add(embeddings)

def answer_question(question):

    query_embedding = model.encode(
        [question]
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k=3
    )

    context = "\n\n".join(
        [chunks[idx] for idx in indices[0]]
    )

    prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = generator(
        prompt,
        max_new_tokens=100
    )

    return response[0]["generated_text"]
    
demo = gr.Interface(
    fn=answer_question,
    inputs=gr.Textbox(
        label="Ask a Question"
    ),
    outputs="text",
    title="PDF Question Answering System"
)

demo.launch()