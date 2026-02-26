"""
Multi-Query RAG.
"""

from __future__ import annotations
from loguru import logger

# rag包中的定义。
from rag.langgraph_retrievers.qdrant_retrievers.multi_query_retriever import QdrantMultiQueryRetriever
# 正常导入。
from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.runnables import RunnableConfig


class MultiQueryRAG(QdrantMultiQueryRetriever):
    # 为接入当前MAS进行的重写。
    async def process_state(
        self,
        state: FinalMASState,
        config: RunnableConfig,
    ) -> dict:
        # query和current_message共用同一字段以实现统一。
        ## HACK: 根据需求，未来可进行重构。
        query = state.current_message
        result_documents = await self.parallel_search_documents(
            query=query,
            search_configs=self._search_configs,
            search_method=self._search_configs['search_method'],
        )
        return dict(
            current_documents=result_documents,
            current_agent_name='analyst',  # 冗余字段，retriever结果一定会返回analyst。
            last_agent_name='rag',  # Analyst判断的字段。
        )

