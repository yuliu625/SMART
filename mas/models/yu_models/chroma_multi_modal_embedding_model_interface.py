"""

"""

from langchain_core.embeddings import Embeddings


class ChromaMultiModalEmbeddingModel(Embeddings):
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

