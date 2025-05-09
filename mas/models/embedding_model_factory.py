"""
生成embedding model的工厂。
"""

from .yu_models import (
    YuFakeEmbeddingModel,
    ChromaMultiModalEmbeddingModel,
)
from .yu_models import (
    NomicEmbedVisionV15,
    CLIPVitLargePatch14,
    BGEVLLarge,
)
from .embedding_model_info_mapper import EmbeddingModelInfoMapper

from langchain_huggingface import HuggingFaceEmbeddings
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
        if model_key == 'fake':
            return YuFakeEmbeddingModel()
        elif model_key == 'model1':
            return self.get_model1()
        elif model_key == 'model2':
            return self.get_model2()
        elif model_key == 'model3':
            return self.get_model3()
        elif model_key == 'model4':
            return self.get_model4()
        elif model_key == 'model5':
            return self.get_model5()
        elif model_key == 'model6':
            return self.get_model6()

    def get_model1(self):
        embedding_model = HuggingFaceEmbeddings(
            model_name=r"D:\model\nomic-ai\nomic-embed-text-v1.5",
            model_kwargs={
                'trust_remote_code': True,
                # 'device': 'cuda' if torch.cuda.is_available() else 'cpu'
            },
        )
        return embedding_model

    def get_model2(self):
        embedding_model = HuggingFaceEmbeddings(
            model_name=r"D:\model\BAAI\bge-m3",
            model_kwargs={
                'trust_remote_code': True,
                # 'device': 'cuda' if torch.cuda.is_available() else 'cpu'
            },
        )
        return embedding_model

    def get_model3(self):
        embedding_model = HuggingFaceEmbeddings(
            model_name=r"",
            model_kwargs={
                'trust_remote_code': True,
                # 'device': 'cuda' if torch.cuda.is_available() else 'cpu'
            },
        )
        return embedding_model

    def get_model4(self):
        embedding_model = NomicEmbedVisionV15(
            text_model_path=r"D:\model\nomic-ai\nomic-embed-text-v1.5",
            vision_model_path=r"D:\model\nomic-ai\nomic-embed-vision-v1.5",
        )
        return embedding_model

    def get_model5(self):
        embedding_model = CLIPVitLargePatch14(
            model_path=r"D:\model\openai\clip-vit-large-patch14"
        )
        return embedding_model

    def get_model6(self):
        embedding_model = BGEVLLarge(
            model_path=r"D:\model\BAAI\BGE-VL-large"
        )
        return embedding_model


if __name__ == '__main__':
    pass
