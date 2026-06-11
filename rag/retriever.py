from pathlib import Path

from rag.embedder import Embedder
from rag.vector_store import VectorStore


class Retriever:
    """
    Handles document loading, embedding,
    indexing, and retrieval.
    """

    def __init__(self):

        self.embedder = Embedder()
        self.store = None

    def build_from_file(
        self,
        file_path: str,
        chunk_size: int = 500
    ):
        """
        Build vector index from a text file.
        """

        content = Path(file_path).read_text(
            encoding="utf-8"
        )

        chunks = self.embedder.chunk_text(
            content,
            chunk_size=chunk_size
        )

        embeddings = self.embedder.encode(
            chunks
        )

        self.store = VectorStore()

        self.store.add_documents(
            embeddings,
            chunks
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 3
    ):
        """
        Retrieve relevant chunks.
        """

        if self.store is None:
            raise ValueError(
                "Vector store not initialized."
            )

        query_embedding = self.embedder.encode(
            query
        )[0]

        results = self.store.search(
            query_embedding,
            top_k=top_k
        )

        return results

    def get_context(
        self,
        query: str,
        top_k: int = 3
    ):
        """
        Return retrieved chunks as
        a single context string.
        """

        results = self.retrieve(
            query,
            top_k
        )

        return "\n\n".join(
            item["document"]
            for item in results
        )