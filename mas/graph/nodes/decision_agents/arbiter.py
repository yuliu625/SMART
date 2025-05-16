"""
仲裁者。
"""

from ...states import MASState
from ..base_agent import BaseAgent
from mas.utils import JsonOutputParser

from langchain_core.runnables import Runnable
from pydantic import BaseModel
from langchain_core.messages import AIMessage, HumanMessage


class Arbiter(BaseAgent):
    """
    执行最终仲裁决定。

    是LRM。
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

    def run(self, state: MASState):
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

    def arbitrate(self, state: MASState):
        ...

