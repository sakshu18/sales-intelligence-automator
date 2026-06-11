import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


class VectorStore:
    """
    Lightweight vector store using cosine similarity.
    No FAISS dependency required.
    """

    def __init__(self):
        self.documents = []
        self.embeddings = None

    def add_documents(
        self,
        embeddings,
        documents
    ):
        """
        Store embeddings and documents.
        """

        self.embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        self.documents.extend(
            documents
        )

    def search(
        self,
        query_embedding,
        top_k: int = 3
    ):
        """
        Retrieve top-k most similar documents.
        """

        if self.embeddings is None:
            return []

        similarities = cosine_similarity(
            [query_embedding],
            self.embeddings
        )[0]

        top_indices = similarities.argsort()[
            -top_k:
        ][::-1]

        results = []

        for idx in top_indices:

            results.append({
                "document": self.documents[idx],
                "score": float(
                    similarities[idx]
                )
            })

        return results

    def size(self):
        """
        Number of stored documents.
        """

        return len(
            self.documents
        )