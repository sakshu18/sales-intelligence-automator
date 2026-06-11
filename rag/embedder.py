from sentence_transformers import SentenceTransformer


class Embedder:
    """
    Handles text chunking and embeddings
    using Sentence Transformers.
    """

    def __init__(self):
        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def chunk_text(
        self,
        text: str,
        chunk_size: int = 500
    ):
        """
        Split text into chunks for RAG.
        """

        if not text:
            return []

        chunks = []

        for i in range(
            0,
            len(text),
            chunk_size
        ):
            chunks.append(
                text[i:i + chunk_size]
            )

        return chunks

    def encode(self, texts):
        """
        Generate embeddings for text(s).
        """

        if isinstance(texts, str):
            texts = [texts]

        return self.model.encode(
            texts,
            convert_to_numpy=True
        )