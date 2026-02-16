"""
Tests for vector store pipeline.
"""

from __future__ import annotations
import pytest
from loguru import logger

from rag.chroma_vector_store_pipeline import ChromaVectorStorePipeline

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestVectorStorePipeline:
    @pytest.mark.parametrize(
        "markdown_file_path, result_path", [
        (r"D:\dataset\smart\tests\docling_1\000004.md",
         r"D:\dataset\smart\tests\000004",),
    ])
    def test_make_vector_store_via_ollama(
        self,
        markdown_file_path: str | Path,
        result_path: str | Path,
    ):
        markdown_file_path = Path(markdown_file_path)
        result_path = Path(result_path)
        if not result_path.exists():
            # result_path.mkdir(parents=True, exist_ok=True)
            ChromaVectorStorePipeline.make_vector_store_via_ollama(
                markdown_file_path=markdown_file_path,
                headers_to_split_on=[
                    ("#", "Header 1"),
                    ("##", "Header 2"),
                    ("###", "Header 3"),
                    ("####", "Header 4"),
                ],
                ollama_embedding_model_name=r'nomic-embed-text',
                ollama_embedding_model_context_length=8192,
                vector_store_path=result_path,
            )

