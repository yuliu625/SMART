"""
Simple RAG.

整合了各种检索方法，包括:
    - dense
    - sparse
    - multi_vector
    - hybrid
    - all in one
"""

from __future__ import annotations
from loguru import logger

# rag包中的定义。
from rag.langgraph_retrievers.qdrant_retrievers.simple_retriever import QdrantSimpleRetriever
# 正常导入。
from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.runnables import RunnableConfig


class SimpleRAG(QdrantSimpleRetriever):
    # 为接入当前MAS进行的重写。
    async def process_state(
        self,
        state: FinalMASState,
        config: RunnableConfig,
    ) -> dict:
        # query和current_message共用同一字段以实现统一。
        ## HACK: 根据需求，未来可进行重构。
        query = state.current_message
        search_method = self._search_configs['search_method']
        result_documents = []
        match search_method:
            case 'dense':
                result_documents = self.search_documents_via_dense_retrieval(
                    query=query,
                    search_configs=self._search_configs,
                )
            case 'sparse':
                result_documents = self.search_documents_via_sparse_retrieval(
                    query=query,
                    search_configs=self._search_configs,
                )
            case 'multi_vector':
                result_documents = self.search_documents_via_multi_vector(
                    query=query,
                    search_configs=self._search_configs,
                )
            case 'hybrid':
                result_documents = self.hybrid_search_documents(
                    query=query,
                    search_configs=self._search_configs,
                )
            case 'all':
                result_documents = self.all_search_documents(
                    query=query,
                    search_configs=self._search_configs,
                )
            case _:
                result_documents = []
        return dict(
            current_documents=result_documents,
            current_agent_name='analyst',  # 冗余字段，retriever结果一定会返回analyst。
            last_agent_name='rag',  # Analyst判断的字段。
        )

