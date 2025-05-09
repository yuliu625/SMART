"""
各种模型的工厂。

额外构建这个包的原因是:
    - 多模态的支持很少。需要自主实现multi-modal embedding model。
"""

from .embedding_model_factory import EmbeddingModelFactory
from .embedding_model_info_mapper import EmbeddingModelInfoMapper

from .llm_factory import LLMFactory
from .vlm_factory import VLMFactory


from .yu_models import YuFakeEmbeddingModel

