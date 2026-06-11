from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

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
chunk_size = 500

chunks = []

for i in range(0, len(text), chunk_size):
    chunks.append(text[i:i+chunk_size])

print("Chunks:", len(chunks))

# Embeddings
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(chunks)

embeddings = np.array(
    embeddings
).astype("float32")

# FAISS Index
dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(
    dimension
)

index.add(
    embeddings
)

print("Vectors stored:", index.ntotal)

# User Question
query = "Stand up straight with your shoulders back"

# Convert question to embedding
query_embedding = model.encode(
    [query]
).astype("float32")

# Search top 3 matches
distances, indices = index.search(
    query_embedding,
    k=3
)

print("\nQuestion:")
print(query)

print("\nTop Results:\n")

for idx in indices[0]:
    print(chunks[idx])
    print("\n" + "-"*50 + "\n")