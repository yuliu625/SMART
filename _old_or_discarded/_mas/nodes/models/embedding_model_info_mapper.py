"""
所有相关的embedding-model
"""

from pydantic import BaseModel


class EmbeddingModel(BaseModel):
    name: str
    dim: int
    type: str
    path: str


EMBEDDING_MODEL_INFO = dict(
    model1=EmbeddingModel(
        name='nomic-embed-text-v1.5',
        dim=768,
        type='text',
        path=r'D:\model\nomic-ai\nomic-embed-text-v1.5',
    ),
    model2=EmbeddingModel(
        name='bge-m3',
        dim=768,
        type='text',
        path=r'D:\model\BAAI\bge-m3',
    ),
    model3=EmbeddingModel(
        name='',
        dim=768,
        type='text',
        path='nomic-ai/nomic-embed-vision-v1.5',
    ),
    model4=EmbeddingModel(
        name='nomic-embed-vision-v1.5',
        dim=768,
        type='image',
        path=r'D:\model\nomic-ai\nomic-embed-vision-v1.5',
    ),
    model5=EmbeddingModel(
        name='clip-vit-large-patch14',
        dim=768,
        type='image',
        path=r'D:\model\openai\clip-vit-large-patch14',
    ),
    model6=EmbeddingModel(
        name='BGE-VL-large',
        dim=768,
        type='image',
        path=r'D:\model\BAAI\BGE-VL-large',
    ),
    model7=EmbeddingModel(
        name='',
        dim=1,
        type='image',
        path=r'',
    ),
)


class EmbeddingModelInfoMapper:
    def __init__(self):
        ...

    def get_dim(
        self,
        model_key: str,
    ) -> int:
        return EMBEDDING_MODEL_INFO[model_key].dim

    def get_name(
        self,
        model_key: str,
    ) -> str:
        return EMBEDDING_MODEL_INFO[model_key].name

    def get_path(
        self,
        model_key: str,
    ) -> str:
        return EMBEDDING_MODEL_INFO[model_key].path

