"""
生成embedding model的工厂。
"""

from mas.models.yu_models.nomic_embed_vision_v15 import NomicEmbedVisionV15

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
        ...

    def get_qwen_embedding_model(
        self,
        model_name: Annotated[str, "qwen上的embedding_model的名字"] = 'text-embedding-v3',
    ) -> Embeddings:
        embedding_model = OpenAILikeEmbedding(
            model_name=model_name,
            api_base=os.environ['DASHSCOPE_API_BASE_URL'],
            api_key=os.environ['DASHSCOPE_API_KEY'],
        )
        return embedding_model

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
