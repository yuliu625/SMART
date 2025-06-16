"""
验证者。
"""

from __future__ import annotations

from mas.nodes.base_agent import BaseAgent
from mas.schemas.structured_output_format import (
    AgentRequest,
    AgentProcessedResult,
)

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.messages import AnyMessage


class Validator(BaseAgent):
    """
    根据已有信息，反复验证。
    """
    def __init__(
        self,
        chat_prompt_template: ChatPromptTemplate,
        llm: BaseChatModel,
    ):
        super().__init__(
            chat_prompt_template=chat_prompt_template,
            llm=llm,
            max_retries=10,
            is_need_structured_output=True,
            schema_pydantic_base_model=AgentRequest,
            schema_check_type='dict',
        )

    def process_state(
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
        validator_result = self.validate(
            shared_chat_history=state.shared_chat_history,
            remaining_validation_rounds=state.remaining_validation_rounds,
        )
        if state.remaining_validation_rounds == 0:
            # 已经用完验证次数，需要进行仲裁。
            return dict(
                shared_chat_history=validator_result.chat_history,
                current_agent_name='arbiter',
            )
        else:
            # 继续运行。
            return dict(
                shared_chat_history=validator_result.chat_history,
                current_agent_name=validator_result.agent_request.agent_name,
                current_message=validator_result.agent_request.agent_message,
                remaining_validation_rounds=state.remaining_validation_rounds - 1,  # 使用一次验证，更新可验证次数-1。或者去仲裁。
            )

    def validate(
        self,
        shared_chat_history: list[AnyMessage],
        remaining_validation_rounds: int,
    ) -> AgentProcessedResult:
        """

        Args:
            shared_chat_history:
            remaining_validation_rounds:

        Returns:
            AgentProcessedResult:
        """
        shared_chat_history = self._before_call_validator(
            chat_history=shared_chat_history,
            remaining_validation_rounds=remaining_validation_rounds,
        )
        response = self.call_llm_with_retry(chat_history=shared_chat_history)
        agent_request = self.get_structured_output(raw_str=response.content)
        return AgentProcessedResult(
            chat_history=shared_chat_history + [response],
            agent_request=AgentRequest(**agent_request),
        )

    def _before_call_validator(
        self,
        chat_history: list[AnyMessage],
        remaining_validation_rounds: int,
    ) -> list[AnyMessage]:
        """

        Args:
            chat_history:
            remaining_validation_rounds:

        Returns:
            list[AnyMessage]:
        """
        chat_history_ = chat_history.copy()
        # 如果是刚刚初始化的chat-history。里面的message是recognizer写的。
        if len(chat_history_) == 1:
            # 直接返回chat-history，不做处理。
            return chat_history_
        last_round_content = chat_history_[-1].content
        if remaining_validation_rounds == 0:
            # 最后验证提醒。
            last_round_content = (
                last_round_content
                + "\n\n已经用完验证次数，现在必须做出分析结论交给arbiter进行仲裁。"
            )
        else:
            # 一般情况，添加验证次数提示。
            last_round_content = (
                last_round_content
                + f"\n\n还剩{remaining_validation_rounds}次验证次数。"
            )
        chat_history_[-1] = HumanMessage(content=last_round_content)
        return chat_history_

