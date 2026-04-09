"""
multi-agent debate runner
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas.cached_mas_factory import CachedMASFactory
from mas.qdrant_rag_factory import QdrantRAGFactory
from mas.cached_io_methods import CachedIOMethods

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


async def semaphore_wrapper(
    semaphore: asyncio.Semaphore,
    func,
    *args,
    **kwargs,
):
    async with semaphore:
        return await func(*args, **kwargs)


class CachedMultiAgentDebateRunner:
    @staticmethod
    async def single_run_multi_agent_debate_with_simple_rag(

    ):
        raise NotImplementedError

    @staticmethod
    async def single_run_multi_agent_debate_with_multi_query_rag(

    ):
        raise NotImplementedError

    @staticmethod
    async def batch_run_multi_agent_debate_with_simple_rag(

    ):
        raise NotImplementedError

    @staticmethod
    async def batch_run_multi_agent_debate_with_multi_query_rag(

    ):
        raise NotImplementedError

