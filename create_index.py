import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data.txt","r",encoding="utf-8") as f:
    data = f.read()

chunks = data.split("\n\n")
texts = [c.strip() for c in chunks if c.strip()]

embeddings = model.encode(texts)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

os.makedirs("faiss_index",exist_ok=True)

faiss.write_index(index,"faiss_index/index.faiss")

with open("faiss_index/texts.pkl","wb") as f:
    pickle.dump(texts,f)

print("Index created")