"""
验证者。

Decision-Module部分需要具体设计的Agent。
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
        # 重要agent，必须要有输出格式。
        super().__init__(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            main_llm_max_retries=3,
            # 需要结构化输出，确定下一步决策和调用的agent。
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
        """
        Decision-Module最重要的部分，进行分析和决策。

        Args:
            state (MASState): 使用的state。需要字段:
                - decision_shared_messages:
                    - Case1: Surveyor之后的shared_messages。
                    - Case2: Analyst之后的shared_messages。
                - remaining_validation_rounds: 剩余的验证次数。
            config (RunnableConfig): 运行设置。

        Returns:
            dict: 进行更新的字段，包括:
                - decision_shared_messages: 更新了investigator后的shared_messages。
                - current_agent_name: 下一个运行的agent。
                - current_message: investigator对analyst提出的要求。
                - remaining_validation_rounds: 剩余的验证次数。
        """
        # Agent内: 根据甚于验证次数，处理surveyor或analyst的message。
        decision_shared_messages = self.before_call_investigator(
            decision_shared_messages=state.decision_shared_messages,
            remaining_validation_rounds=state.remaining_validation_rounds,
        )
        # Agent内: 获取investigator的分析和决策。
        investigator_result = await self.verify_details(
            decision_shared_messages=decision_shared_messages,
        )
        # 整个MAS: 构建shared_messages。
        decision_shared_messages = self.after_call_investigator(
            investigator_message=investigator_result.ai_message,
            decision_shared_messages=investigator_result.decision_shared_messages,
        )
        # 根据剩余验证轮数调用下一个agent。
        if state.remaining_validation_rounds == 0:
            # 已经用完验证次数，需要进行最终决定。
            # 这个判断是system层级冗余稳定判断。
            return dict(
                decision_shared_messages=decision_shared_messages,
                current_agent_name='adjudicator',  # 这个条件下，该字段是确定和强制的。
                current_message=investigator_result.agent_request.agent_message,  # 为保持一致返回的字段。
                remaining_validation_rounds=state.remaining_validation_rounds - 1,  # 为保持一致返回的字段。
            )
        else:
            # 正常运行。
            # Case1: 请求的是adjudicator，主动结束分析。
            # Case2: 请求analyst，对于某些details要求分析。
            return dict(
                decision_shared_messages=decision_shared_messages,
                current_agent_name=investigator_result.structured_output.agent_name,
                current_message=investigator_result.agent_request.agent_message,
                remaining_validation_rounds=state.remaining_validation_rounds-1,  # 使用一次验证，更新可验证次数-1。或者去仲裁。
            )

    # ====主要方法。====
    async def verify_details(
        self,
        decision_shared_messages: list[AnyMessage],
    ) -> BaseAgentResponse:
        # 一般执行请求。
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
            ] + decision_shared_messages,
        )
        return response

    # ====工具方法。====
    def before_call_investigator(
        self,
        decision_shared_messages: list[AnyMessage],
        remaining_validation_rounds: int,
    ) -> list[AnyMessage]:
        """
        处理给予Investigator的全部context。

        Conditions:
            - Case1: Surveyor以HumanMessage进行的初始启动。
                - Case1.1: 初始启动。
            - Case2: Analyst提交的分析结论。
                - Case2.1: 常规调查流程中。
                - Case2.2: 以及用完所有验证次数。

        Args:
            decision_shared_messages (list[AnyMessage]): 由Surveyor初始化，或由Analyst提交的shared_messages。
            remaining_validation_rounds (int): 剩余验证次数。

        Returns:
            list[AnyMessage]: 根据各种条件，添加引导后的，提交给Investigator的shared_messages。
        """
        decision_shared_messages_ = decision_shared_messages.copy()
        # 如果是刚刚初始化的decision_shared_messages。里面的message是recognizer写的。
        if len(decision_shared_messages_) == 1:
            # 直接返回shared_messages，不做处理。
            return decision_shared_messages_
        # else: 正常和analyst进行交互的轮次。
        # 最后一轮message是:
        # Case1: Surveyor以HumanMessage进行的初始启动。
        # Case2: Analyst提交的分析结论。
        assert isinstance(decision_shared_messages_[-1], HumanMessage)
        # 提取最后一轮的message。
        last_round_content = decision_shared_messages_[-1].content
        # 根据剩余验证次数，添加引导prompt。
        if remaining_validation_rounds == 0:
            # Case2.2: 以及用完所有验证次数。
            # 最后验证提醒。
            last_round_content = (
                last_round_content
                + f"\n\n还剩{remaining_validation_rounds}次验证次数。"
                + "\n\n已经用完调查次数，现在必须做出最终结论交给Adjudicator做出最终结论。"
            )
        else:
            # Case1.1: 初始启动。
            # Case2.1: 常规调查流程中。
            # 一般情况，添加验证次数提示。
            last_round_content = (
                last_round_content
                + f"\n\n还剩{remaining_validation_rounds}次验证次数。"
                + f"你还可以提出一些点进行进一步的调查，或交给Adjudicator做出最终结论。"
            )
        decision_shared_messages_[-1] = HumanMessage(content=last_round_content)
        return decision_shared_messages_

    # ====工具方法。====
    def after_call_investigator(
        self,
        investigator_message: AIMessage,
        decision_shared_messages: list[AnyMessage],
    ) -> list[AnyMessage]:
        """
        对于shared_messages，当前investigator为主要使用者。

        Args:
            investigator_message (AIMessage): Investigator的message。但是没有标记tag。
            decision_shared_messages (list[AnyMessage]): 在Investigator之前的decision_shared_messages。

        Returns:
            list[AnyMessage]: Investigator的message被标记，全部完整的decision_shared_messages。
        """
        assert isinstance(investigator_message, AIMessage)
        # 标注身份。
        investigator_last_message_content = ContentAnnotator.annotate_with_html_comment(
            tag='investigator',
            original_text=investigator_message.content,
        )
        # 构建decision_shared_messages。
        decision_shared_messages = decision_shared_messages + [
            AIMessage(content=investigator_last_message_content),  # 把investigator的信息放进去。
        ]
        return decision_shared_messages

