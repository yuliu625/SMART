"""

"""

from ...states import MASState
from ..base_agent import BaseAgent
from mas.utils import JsonOutputParser

from langchain_core.messages import AnyMessage, AIMessage
from langchain_core.runnables import Runnable
from pydantic import BaseModel


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
        self.llm_chain = llm_chain
        self.structured_output_format = structured_output_format

    def run(self, state: MASState):
        """

        Args:
            state:

        Returns:

        """
        to_be_updated_state = {}
        response = self.analyze(chat_history=state.chat_history)
        request = self.get_agent_request(response=response)
        if request['agent_name'] == 'validator':
            # 不需要更多的信息。
            to_be_updated_state['more_information'] = False
        else:  # request['agent_name'] == 'document_reader'
            # 需要更多的信息，并且需要指定查询内容。
            to_be_updated_state['more_information'] = True
            to_be_updated_state['current_query'] = request['message']

    def analyze(
        self,
        chat_history: list[AnyMessage]
    ) -> AIMessage:
        response = self.call_llm_chain(chat_history=chat_history)
        return response


