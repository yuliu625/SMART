"""
支持方，预设正标签。

multi-agent debate 中的 agent 因 ablation study ，不与 investigator 进行交互。
"""

from __future__ import annotations
from loguru import logger

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
from mas.utils.content_annotator import ContentAnnotator
from mas.utils.document_merger import DocumentMerger

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING, Literal, cast
if TYPE_CHECKING:
    from mas.schemas.multi_agent_debate_state import MultiAgentDebateState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage
    from langchain_core.documents import Document
    from pydantic import BaseModel


class Proponent(BaseAgent):
    """
    持有同意立场的 agent 。
    """
    def __init__(
        self,
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        # formatter 相关。
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ):
        # HACK: 特殊实现，提取的 query 是给对方 agent 的。
        super().__init__(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            main_llm_max_retries=3,
            # 需要结构化输出。
            is_need_structured_output=True,
            formatter_llm=formatter_llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
            formatter_llm_system_message=formatter_llm_system_message,
            formatter_llm_max_retries=3,
        )
        self.main_llm_system_message = main_llm_system_message

    async def process_state(
        self,
        state: MultiAgentDebateState,
        config: RunnableConfig,
    ) -> dict:
        debate_process = self.before_call_proponent(
            remaining_debate_rounds=state.remaining_debate_rounds,
            current_message=state.current_message,
            documents=state.current_documents,
            decision_shared_messages=state.decision_shared_messages,
        )
        logger.trace(f"\nDebate Process: \n{debate_process}")
        debate_result = await self.read_debate_process_and_documents(
            decision_shared_messages=debate_process,
        )
        debate_process = self.after_call_proponent(
            proponent_message=debate_result.ai_message,
            decision_shared_messages=debate_process,
        )
        logger.trace(f"\nDebate Process: \n{debate_process}")
        return dict(
            decision_shared_messages=debate_process,
            current_message=debate_result.structured_output.agent_message,
            current_agent_name='opponent_rag',
            last_agent_name='proponent',
        )

    # ==== 主要方法。 ====
    async def read_debate_process_and_documents(
        self,
        decision_shared_messages: list[AnyMessage],
    ) -> BaseAgentResponse:
        # 获取 llm 响应。
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
            ] + decision_shared_messages,
        )
        return response

    # ==== 工具方法。 ====
    def before_call_proponent(
        self,
        remaining_debate_rounds: int,
        current_message: str,
        documents: list[Document],
        decision_shared_messages: list[AnyMessage],
    ) -> list[AnyMessage]:
        assert len(decision_shared_messages) == 1
        # 整合新的文档。
        document_content = DocumentMerger.merge_text_documents(
            text_documents=documents,
        )
        document_content = f"Query: \n {current_message}\n Result: \n{document_content}"
        rag_message_content = ContentAnnotator.safe_annotate_with_html(
            tag='rag',
            original_text=document_content,
        )
        # 构建 debate_process 。
        ## 不做复杂处理，共享记忆池。
        debate_process_content = decision_shared_messages[0].content + "\n" + rag_message_content
        debate_process = [
            HumanMessage(content=debate_process_content),
        ]
        assert len(debate_process) == 1
        return debate_process

    # ==== 工具方法。 ====
    def after_call_proponent(
        self,
        proponent_message: AIMessage,
        decision_shared_messages: list[AnyMessage],
    ) -> list[AnyMessage]:
        assert isinstance(proponent_message, AIMessage)
        assert len(decision_shared_messages) == 1
        # 标注身份。
        proponent_last_message_content = ContentAnnotator.safe_annotate_with_html(
            tag='proponent',
            original_text=proponent_message.content,
        )
        # 构建 debate_process 。
        ## 不做复杂处理，共享记忆池。
        debate_process_content = decision_shared_messages[0].content + "\n" + proponent_last_message_content
        debate_process = [
            HumanMessage(content=debate_process_content),
        ]
        assert len(debate_process) == 1
        return debate_process

