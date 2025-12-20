"""
验证者。

Decision-Module部分需要具体设计的Agent。
"""

from __future__ import annotations

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
from mas.utils.content_annotator import ContentAnnotator
# from mas.schemas.structured_output_format import (
#     AgentRequest,
#     AgentProcessedResult,
# )

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage
    from pydantic import BaseModel


class Investigator(BaseAgent):
    """
    根据已有信息，反复验证。
    """
    def __init__(
        self,
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        # formatter相关，Validator一定需要formatter。
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ):
        # 基本的agent，不对于输出进行限制。
        super().__init__(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            main_llm_max_retries=3,
            # 不需要结构化输出。
            is_need_structured_output=True,
            formatter_llm=formatter_llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
            formatter_llm_system_message=formatter_llm_system_message,
            formatter_llm_max_retries=3,
        )
        self.main_llm_system_message = main_llm_system_message

    async def process_state(
        self,
        state: DecisionState,
        config: RunnableConfig,
    ) -> dict:
        """

        Args:
            state:
            config (RunnableConfig): 运行设置。

        Returns:
            dict: 进行更新的字段，包括:
        """
        # 处理
        validator_result = await self.validate(
            decision_shared_messages=state.decision_shared_messages,
            # remaining_validation_rounds=state.remaining_validation_rounds,
        )
        if state.remaining_validation_rounds == 0:
            # 已经用完验证次数，需要进行仲裁。
            return dict(
                shared_chat_history=validator_result.chat_history,
                current_agent_name='adjudicator',
            )
        else:
            # 继续运行。
            return dict(
                shared_chat_history=validator_result.chat_history,
                current_agent_name=validator_result.agent_request.agent_name,
                current_message=validator_result.agent_request.agent_message,
                remaining_validation_rounds=state.remaining_validation_rounds-1,  # 使用一次验证，更新可验证次数-1。或者去仲裁。
            )

    # ====主要方法。====
    async def validate(
        self,
        decision_shared_messages: list[AnyMessage],
    ) -> BaseAgentResponse:
        """

        Args:
            decision_shared_messages:

        Returns:
            BaseAgentResponse:
        """
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
            ] + decision_shared_messages,
        )
        return response

    # ====工具方法。====
    def before_call_validator(
        self,
        decision_shared_messages: list[AnyMessage],
        remaining_validation_rounds: int,
    ) -> list[AnyMessage]:
        """
        处理给予Validator的全部context。

        Conditions:
            - 第一轮:
            - 中间轮:
            - 最终轮:

        Args:
            decision_shared_messages:
            remaining_validation_rounds:

        Returns:
            list[AnyMessage]:
        """
        decision_shared_messages_ = decision_shared_messages.copy()
        # 如果是刚刚初始化的decision_shared_messages。里面的message是recognizer写的。
        if len(decision_shared_messages_) == 1:
            # 直接返回chat-history，不做处理。
            return decision_shared_messages_
        # else: 正常和analyst进行交互的轮次。
        # 提取最后一轮的message。
        last_round_content = decision_shared_messages_[-1].content
        #
        if remaining_validation_rounds == 0:
            # 最后验证提醒。
            last_round_content = (
                last_round_content
                + "\n\n已经用完验证次数，现在必须做出最终结论交给Arbiter进行仲裁。"
            )
        else:
            # 一般情况，添加验证次数提示。
            last_round_content = (
                last_round_content
                + f"\n\n还剩{remaining_validation_rounds}次验证次数。"
            )
        decision_shared_messages_[-1] = HumanMessage(content=last_round_content)
        return decision_shared_messages_

    # ====工具方法。====
    def after_call_validator(
        self,
        validator_message: AIMessage,
        decision_shared_messages: list[AnyMessage],
    ) -> list[AnyMessage]:
        ...

