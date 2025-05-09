"""
加载vector-store的方法。
"""

from langchain_chroma import Chroma

from pathlib import Path

from langchain_core.embeddings import Embeddings
from langchain_core.vectorstores import VectorStore


def load_vector_store(
    persist_dir: str | Path,
    embedding_model: Embeddings,
    collection_name: str = None,
) -> VectorStore:
    if collection_name is None:
        vector_store = Chroma(
            persist_directory=str(persist_dir),
            embedding_function=embedding_model,
        )
    else:
        vector_store = Chroma(
            persist_directory=str(persist_dir),
            embedding_function=embedding_model,
            collection_name=collection_name,
        )
    return vector_store

