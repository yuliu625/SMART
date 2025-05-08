"""

"""

from langchain_core.embeddings import Embeddings

import asyncio


class MyEmbedding(Embeddings):
    def __init__(self, ):
        ...

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        pass

    def embed_query(self, inputs: dict) -> list[float]:
        pass

    def embed_image(
        self,
    ):
        ...


if __name__ == '__main__':
    pass
