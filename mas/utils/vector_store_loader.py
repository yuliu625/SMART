"""
加载默认路径的vector-store。
"""

from mas.nodes.models import EmbeddingModelFactory, YuFakeEmbeddingModel

from langchain_chroma import Chroma
from pathlib import Path

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.embeddings import Embeddings
    from langchain_core.vectorstores import VectorStore


class VectorStoreLoader:
    def __init__(
        self,
        file_tree,
    ):
        self.file_tree = file_tree

    def get_document_store(
        self,
        modality: str,
        loading_method: str,
    ) -> VectorStore:
        if modality == 'text':
            persist_dir = self.sub_dir_dict.text_document_store_dir / loading_method
        else:  # if modality == 'image':
            persist_dir = self.sub_dir_dict.image_document_store_dir / loading_method
        document_store = Chroma(
            persist_directory=str(persist_dir),
            embedding_function=YuFakeEmbeddingModel(),
        )
        return document_store

    def get_vector_store(
        self,
        modality: str,
        loading_method: str,
        embedding_method: str,
    ) -> VectorStore:
        if modality == 'text':
            persist_dir = self.sub_dir_dict.text_vector_store_dir / f"{embedding_method}--{loading_method}"
        else:  # if modality == 'image':
            persist_dir = self.sub_dir_dict.image_vector_store_dir / f"{embedding_method}--{loading_method}"
        embedding_model = self._get_embedding_model(embedding_method=embedding_method)
        vector_store = Chroma(
            persist_directory=str(persist_dir),
            embedding_function=embedding_model,
        )
        return vector_store

    def _get_embedding_model(
        self,
        embedding_method: str,
    ) -> Embeddings:
        embedding_model_factory = EmbeddingModelFactory()
        embedding_model = embedding_model_factory.get_embedding_model_by_key(
            model_key=embedding_method,
        )
        return embedding_model

