"""
最基础的retriever。

该实现根据当前MAS的需要重写了process_state方法。(暂时使用继承实现。)
"""

from __future__ import annotations
from loguru import logger

# rag包中的定义。
from rag.langgraph_retrievers.simple_retriever import SimpleRetriever
# 正常导入。
from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.runnables import RunnableConfig


class SimpleRAG(SimpleRetriever):
    # 为接入当前MAS进行的重写。
    async def process_state(
        self,
        state: FinalMASState,
        config: RunnableConfig,
    ) -> dict:
        # query和current_message共用同一字段以实现统一。
        ## HACK: 根据需求，未来可进行重构。
        query = state.current_message
        result_documents = await self.search_documents_by_mmr(
            query=query,
            search_configs=self._search_configs,
        )
        return dict(
            current_documents=result_documents,
        )

