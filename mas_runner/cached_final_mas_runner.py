"""
使用 cache 加速 MAS 的自动运行。

实验运行的时，约定 embedding-model 使用 qdrant 集成的 fastembed 运行。

特殊情况:
    - 该 runner 硬编码 graph 超级步最大限制为 100 次。
"""

from __future__ import annotations
from loguru import logger

from mas.cached_mas_factory import CachedMASFactory
from mas.qdrant_rag_factory import QdrantRagFactory
from mas.cached_io_methods import CachedIOMethods

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class CachedFinalMASRunner:
    @staticmethod
    async def run_final_mas():
        ...

