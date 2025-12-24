"""

"""

from _old_or_discarded._mas.utils import get_default_dir
from _old_or_discarded._mas.utils import VectorStoreLoader, get_all_documents

from pathlib import Path

from langchain_core.documents import Document
from langchain_core.vectorstores import VectorStore


class TextIndexer:
    """
    指定冷启动的vector_store，给出embedding_model，生成对应的embedding。
    """
    def __init__(
        self,
        base_dir: str | Path,
    ):
        self.vector_store_loader = VectorStoreLoader(
            base_dir=base_dir,
        )
        self.default_dir = get_default_dir(base_dir=base_dir)

    def run(
        self,
        loading_method: str,
        embedding_method: str,
    ):
        self.generate_vector_store_from_document_store(
            loading_method=loading_method,
            embedding_method=embedding_method,
        )

    def generate_vector_store_from_txt(
        self,
        loading_method: str,
        embedding_method: str,
    ):
        ...

    def generate_vector_store_from_document_store(
        self,
        loading_method: str,
        embedding_method: str,
    ):
        documents = self.get_documents(loading_method=loading_method)
        vector_store = self.get_vector_store(loading_method=loading_method, embedding_method=embedding_method)
        vector_store.add_texts(
            texts=[document.page_content for document in documents],
            metadatas=[self.get_metadata(document.metadata, embedding_method) for document in documents],
        )
        return vector_store

    def get_documents(
        self,
        loading_method: str,
    ) -> list[Document]:
        document_store = self.get_document_store(loading_method=loading_method)
        documents = get_all_documents(document_store)
        return documents

    def get_document_store(
        self,
        loading_method: str,
    ) -> VectorStore:
        document_store = self.vector_store_loader.get_document_store(
            modality='text',
            loading_method=loading_method,
        )
        return document_store

    def get_vector_store(
        self,
        loading_method: str,
        embedding_method: str,
    ) -> VectorStore:
        vector_store = self.vector_store_loader.get_vector_store(
            modality='text',
            loading_method=loading_method,
            embedding_method=embedding_method,
        )
        return vector_store

    def get_metadata(
        self,
        document_store_metadata: dict,
        embedding_method: str,
    ) -> dict:
        metadata = document_store_metadata.copy()
        metadata['embedding_method'] = embedding_method
        return metadata


