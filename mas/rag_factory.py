"""
构造rag的工厂。

配合mas_factory使用。
"""

from __future__ import annotations
from loguru import logger

from rag_nodes.chroma_rag_builder import ChromaRAGBuilder

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class RagFactory:
    ...

