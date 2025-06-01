"""
验证者。
"""

from __future__ import annotations

from ..base_agent import BaseAgent

from langchain_core.messages import AnyMessage, HumanMessage, AIMessage

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import Runnable
    from langchain_core.language_models import BaseChatModel
    from langchain_core.prompts import ChatPromptTemplate


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
            is_need_structured_output=False,
            schema_pydantic_base_model=None,
            schema_check_type='dict',
        )

    def process_state(self, state: DecisionState) -> dict:
        state_to_be_updated = self.get_state_to_be_updated(
            validator_chat_history=state.validator_chat_history,
            remaining_validation_rounds=state.remaining_validation_rounds,
            arbiter_context=state.arbiter_context,
        )
        return state_to_be_updated

    def get_state_to_be_updated(
        self,
        validator_chat_history: list[AnyMessage],
        remaining_validation_rounds: int,
        arbiter_context: list[str],
    ) -> dict:
        state_to_be_updated = {}
        response = self.validate(
            chat_history=validator_chat_history,
            remaining_validation_rounds=remaining_validation_rounds,
        )
        agent_request = self.get_agent_request(response)
        # 无论怎么样，记录本次validator的分析。
        state_to_be_updated['validator_chat_history'] = validator_chat_history + [response]
        # 无论怎么样，让arbiter看到记录。
        state_to_be_updated['arbiter_context'] = arbiter_context + [(
            "<!--validator-start-->\n\n"
            + response.content
            + "\n\n<!--validator-end-->"
        )]
        if agent_request['agent_name'] == 'arbiter' or remaining_validation_rounds == 0:
            # 不需要更多的检验。
            # 控制，去仲裁。
            state_to_be_updated['current_agent_name'] = 'arbiter'
        else:  # agent_request['agent_name'] in ['control_analyst', 'financial_analyst', 'strategic_analyst']
            # 需要进行验证。
            # 控制，去对应的analyst。
            state_to_be_updated['current_agent_name'] = agent_request['agent_name']
            # 说明对应analyst需要进一步分析的内容。
            state_to_be_updated['current_message'] = agent_request['message']
            # 使用一次验证，更新可验证次数-1。
            state_to_be_updated['remaining_validation_rounds'] = remaining_validation_rounds - 1
        return state_to_be_updated

    def validate(
        self,
        chat_history: list[AnyMessage],
        remaining_validation_rounds: int,
    ) -> AIMessage:
        # 这里可以直接请求，因为analyst已经将分析的结果以HumanMessage写到validator的chat-history里了，并且已标明身份。
        if remaining_validation_rounds == 0:
            chat_history = self._process_last_round_validation(chat_history)
        response = self.call_llm_chain(chat_history=chat_history)
        return response

    def _process_last_round_validation(
        self,
        chat_history: list[AnyMessage],
    ) -> list[AnyMessage]:
        last_round_content = chat_history[-1].content
        last_round_content = last_round_content + "\n\n已经用完验证次数，这次必须做出小结交给arbiter进行仲裁。"
        chat_history[-1] = HumanMessage(content=last_round_content)
        return chat_history

