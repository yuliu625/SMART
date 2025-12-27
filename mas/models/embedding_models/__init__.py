"""
基于Embeddings-interface构建的各种embedding-model。
"""

from .yu_fake_embedding_model import YuFakeEmbeddingModel
from .chroma_multi_modal_embedding_model_interface import ChromaMultiModalEmbeddingModel

# 小型multi-modal-embedding-model。
from .clip_vit_embedding_model import CLIPVitEmbeddingModel
from .nomic_embed_vision_v15 import NomicEmbedVisionV15
from .bge_vl import BGEVL

# 基于VLM的embedding-model。
from .colnomic_embed_multimodal import ColnomicEmbedMultimodal

