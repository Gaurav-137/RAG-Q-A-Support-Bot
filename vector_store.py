import faiss
import numpy as np

class VectorStore:
    def __init__(self, dimension=1536):
        self.index = faiss.IndexFlatL2(dimension)
        self.documents = []

    def add(self, embeddings, docs):
        vectors = np.array(embeddings).astype("float32")
        self.index.add(vectors)
        self.documents.extend(docs)

    def search(self, query_embedding, k=3):
        query_vector = np.array([query_embedding]).astype("float32")
        distances, indices = self.index.search(query_vector, k)

        results = []
        for i in indices[0]:
            if i < len(self.documents):
                results.append(self.documents[i])

        return results