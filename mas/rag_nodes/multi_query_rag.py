"""
multi-query retriever。

该实现根据当前MAS的需要重写了process_state方法。
"""

from __future__ import annotations
from loguru import logger

# rag包中的定义。
from rag.langgraph_retrievers.multi_query_retriever import MultiQueryRetriever
# 正常导入。
from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.runnables import RunnableConfig


class MultiQueryRAG(MultiQueryRetriever):
    async def process_state(
        self,
        state,
        config: RunnableConfig,
    ) -> dict:
        ...

