"""
一个假的embedding-model。
"""

from langchain_core.embeddings import Embeddings


class YuFakeEmbeddingModel(Embeddings):
    """

    """
    def __init__(
        self,
    ):
        pass

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return self.embed_text(texts)

    def embed_query(self, query: str) -> list[float]:
        return self.embed_text([query])[0]

    def embed_text(
        self,
        inputs: list[str]
    ) -> list[list[float]]:
        return [[0.0] for _ in range(len(inputs))]

    def embed_image(
        self,
        uris: list[str],
    ) -> list[list[float]]:
        return [[0.0] for _ in range(len(uris))]

