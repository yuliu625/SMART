"""
仲裁者。
"""

from __future__ import annotations

from ..base_agent import BaseAgent

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import Runnable
    from langchain_core.language_models import BaseChatModel
    from langchain_core.prompts import ChatPromptTemplate


class Arbiter(BaseAgent):
    """
    执行最终仲裁决定。

    是LRM。
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
        # 合并所有的讨论记录。
        arbiter_message_content = '\n\n'.join(state.arbiter_context)
        # 使用llm-chain。
        chat_history = [HumanMessage(content=arbiter_message_content)]
        response = self.call_llm_chain(chat_history=chat_history)
        agent_request = self.get_agent_request(response)
        return {
            'arbiter_chat_history': chat_history + [response],
            'arbiter_decision': agent_request,
        }

    def arbitrate(self, state: DecisionState):
        ...

