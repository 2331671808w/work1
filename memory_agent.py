import faiss
import numpy as np
from openai import OpenAI
from config import OPENAI_API_KEY, EMBED_MODEL

client = OpenAI(api_key=OPENAI_API_KEY)

class MemoryAgent:
    def __init__(self):
        self.dimension = 1536
        self.index = faiss.IndexFlatL2(self.dimension)
        self.memories = []

    def embed(self, text):
        res = client.embeddings.create(
            model=EMBED_MODEL,
            input=text
        )
        return np.array(res.data[0].embedding, dtype="float32")

    def add_memory(self, text):
        emb = self.embed(text)
        self.index.add(np.array([emb]))
        self.memories.append(text)

    def search(self, query, k=3):
        if not self.memories:
            return []
        emb = self.embed(query)
        D, I = self.index.search(np.array([emb]), k)
        return [self.memories[i] for i in I[0] if i < len(self.memories)]
