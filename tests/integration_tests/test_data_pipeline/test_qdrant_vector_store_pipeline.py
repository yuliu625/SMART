"""
Tests for qdrant based vector store pipeline.
"""

from __future__ import annotations
import pytest
from loguru import logger

from rag.qdrant_vector_store_pipeline import (
    QdrantVectorStorePipeline,
)

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestQdrantVectorStorePipeline:
    def test_make_qdrant_vector_store(
        self,
    ):
        result = QdrantVectorStorePipeline.make_vector_store_via_native_bge_m3(
            markdown_file_path=r"D:\dataset\smart\tests\docling_1\000004.md",
            headers_to_split_on=[
                ("#", "Header 1"),
                ("##", "Header 2"),
                ("###", "Header 3"),
                ("####", "Header 4"),
            ],
            embedding_model_name_or_path=r"D:\model\BAAI\bge-m3",
            embedding_model_configs=dict(batch_size=1),
            vector_store_path='./t_qdrant'
        )
        logger.info(f"\nPipeline Result: \n{result}")

