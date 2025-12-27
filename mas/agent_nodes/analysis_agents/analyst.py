"""
进行详细分析的Agent。

Analysis-Module的分析控制。
基于context-engineering，切换各种专家agent。
"""

from __future__ import annotations

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
from mas.utils.content_annotator import ContentAnnotator

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.mas_state import MASState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage
    from pydantic import BaseModel


class Analyst(BaseAgent):
    """
    执行具体分析的analyst。
    """
    def __init__(
        self,
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        # formatter相关，对于这个agent可以以不是必需的方法来实现。
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ):
        # 需要显式做出最终决策的agent。
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
        state: MASState,
        config: RunnableConfig,
    ) -> dict:
        ...

    # ====主要方法。====
    async def read_documents(
        self,
        analysis_messages: list[AnyMessage],
    ) -> BaseAgentResponse:
        # 获取llm响应。
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
            ] + analysis_messages,
        )
        return response


