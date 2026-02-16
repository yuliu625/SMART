"""
使用 cache 加速 Sequential workflow 的自动运行。

实验运行的时，约定 embedding-model 使用 qdrant 集成的 fastembed 运行。
"""

from __future__ import annotations
from loguru import logger

from mas.cached_mas_factory import CachedMASFactory
from mas.qdrant_rag_factory import QdrantRagFactory
from mas.cached_io_methods import CachedIOMethods

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class CachedSequentialWorkflowRunner:
    @staticmethod
    async def run_sequential_workflow_with_simple_rag():
        ...

    @staticmethod
    async def run_sequential_workflow_with_multi_query_rag():
        ...

