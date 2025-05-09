"""
生成embedding model的工厂。
"""

from .yu_models.nomic_embed_vision_v15 import NomicEmbedVisionV15
from .embedding_model_info_mapper import EmbeddingModelInfoMapper

import os

from langchain_core.embeddings import Embeddings
from typing import Annotated


class EmbeddingModelFactory:
    """
    各种embedding-model的工厂。

    实现方法有:
        - OpenAILikeEmbedding，云API请求。
        - HuggingFaceEmbedding，本地推理。
        - BaseEmbeddingModel，我具体实现。
    """
    def __init__(self):
        self.embedding_model_info_mapper = EmbeddingModelInfoMapper()

    def get_embedding_model_by_key(
        self,
        model_key: str,
    ) -> Embeddings:
        # embedding_model = HuggingFaceEmbedding(
        #     # model_name=r"D:\model\nomic-ai\colnomic-embed-multimodal-7b",
        #     model_name=r"D:\model\nomic-ai\nomic-embed-text-v1.5",
        #     trust_remote_code=True
        # )
        # return embedding_model
        my_embedding = NomicEmbedVisionV15(
            text_model_path=r"D:\model\nomic-ai\nomic-embed-text-v1.5",
            vision_model_path=r"D:\model\nomic-ai\nomic-embed-vision-v1.5",
        )
        return my_embedding


if __name__ == '__main__':
    pass
