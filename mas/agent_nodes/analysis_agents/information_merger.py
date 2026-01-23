"""
Information Merger.

实际为静态处理node，仅sequential workflow中会使用。
"""

from __future__ import annotations
from loguru import logger

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
from mas.utils.content_annotator import ContentAnnotator
from mas.utils.document_merger import DocumentMerger

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.sequential_mas_state import SequentialMASState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage
    from langchain_core.documents import Document
    from pydantic import BaseModel


class InformationMerger:
    async def process_state(
        self,
        state: SequentialMASState,
        config: RunnableConfig,
    ) -> dict:
        rag_result = self.process_rag_results(
            current_agent_message=state.current_message,
            documents=state.current_documents,
        )
        return dict()

    def process_rag_results(
        self,
        current_agent_message: str,
        documents: list[Document],
    ) -> HumanMessage:
        document_content = DocumentMerger.merge_text_documents(
            text_documents=documents,
        )
        document_content = f"Query: \n {current_agent_message}\n Result: \n{document_content}"
        rag_message_content = ContentAnnotator.annotate_with_html_comment(
            tag='rag',
            original_text=document_content,
        )
        return HumanMessage(content=rag_message_content)

    def submit_rag_results(
        self,
        rag_result: HumanMessage,
    ) -> HumanMessage:
        ...

