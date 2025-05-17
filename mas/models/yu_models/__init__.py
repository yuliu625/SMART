"""
基于Embeddings-interface构建的各种embedding-model。


"""

from .yu_fake_embedding_model import YuFakeEmbeddingModel
from .chroma_multi_modal_embedding_model_interface import ChromaMultiModalEmbeddingModel

from .clip_vit_large_patch14 import CLIPVitLargePatch14
from .nomic_embed_vision_v15 import NomicEmbedVisionV15
from .bge_vl_large import BGEVLLarge

from .colnomic_embed_multimodal_7b import ColnomicEmbedMultimodal

