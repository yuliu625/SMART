"""

"""

from ...states import MASState
from ..base_agent import BaseAgent

from langchain_core.messages import AnyMessage, AIMessage, HumanMessage
from langchain_core.runnables import Runnable
from pydantic import BaseModel
from typing import Literal


class BaseAnalyst(BaseAgent):
    """
    基础分析者。
    """
    def __init__(
        self,
        llm_chain: Runnable,
        structured_output_format: type[BaseModel],
    ):
        super().__init__(
            llm_chain=llm_chain,
            is_need_structured_output=True,
            structured_output_format=structured_output_format,
        )

    def run(self, state: MASState):
        """

        Args:
            state:

        Returns:

        """
        ...

    def get_state_to_be_updated(
        self,
        this_agent_name: Literal['control', 'financial', 'strategic'],
        analyst_chat_history: list[AnyMessage],
        validator_chat_history: list[AnyMessage],
        remaining_retrieve_rounds: int,
    ):
        state_to_be_updated = {}
        response = self.analyze(
            chat_history=analyst_chat_history,
            remaining_retrieve_rounds=remaining_retrieve_rounds,
        )
        agent_request = self.get_agent_request(response=response)
        if agent_request['agent_name'] == 'validator':
            # 不需要更多的信息。
            state_to_be_updated['current_agent_name'] = 'validator'
            state_to_be_updated['more_information'] = False
            state_to_be_updated[f'{this_agent_name}_analyst_chat_history'] = analyst_chat_history + [response]
            state_to_be_updated['validator_chat_history'] = validator_chat_history + [
                HumanMessage(content=(
                    f"<!--{this_agent_name}-analyst-start-->\n\n"
                    + response.content
                    + f"\n\n<!--{this_agent_name}-analyst-end-->"
                ))
            ]
            # 重置可查询次数。
            state_to_be_updated['remaining_retrieve_rounds'] = 5
        else:  # agent_request['agent_name'] == 'document_reader'
            # 需要更多的信息，并且需要指定查询内容。
            state_to_be_updated['current_agent_name'] = f'{this_agent_name}_document_reader'
            state_to_be_updated['more_information'] = True
            state_to_be_updated[f'{this_agent_name}_analyst_chat_history'] = analyst_chat_history + [response]
            state_to_be_updated['current_message'] = agent_request['message']
            # 使用一次查询。更新可查询次数-1。
            state_to_be_updated['remaining_retrieve_rounds'] = remaining_retrieve_rounds - 1
        return state_to_be_updated

    def analyze(
        self,
        chat_history: list[AnyMessage],
        remaining_retrieve_rounds: int,
    ) -> AIMessage:
        # 这里可以直接请求，因为document-reader已经将阅读的结果以HumanMessage写到analyst的chat-history里了。
        response = self.call_llm_chain(chat_history=chat_history)
        return response

