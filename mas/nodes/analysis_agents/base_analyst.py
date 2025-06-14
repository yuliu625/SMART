"""
基础分析agent的定义。
"""

from __future__ import annotations

from mas.nodes.base_agent import BaseAgent
from mas.schemas.structured_output_format import AgentRequest

from langchain_core.messages import AIMessage, HumanMessage

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from mas.schemas.analysis_state import AnalysisState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage
    from pydantic import BaseModel


class BaseAnalyst(BaseAgent):
    """
    基础分析者。
    """
    def __init__(
        self,
        agent_name: str,
        chat_prompt_template: ChatPromptTemplate,
        llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
    ):
        super().__init__(
            chat_prompt_template=chat_prompt_template,
            llm=llm,
            max_retries=10,
            is_need_structured_output=True,
            schema_pydantic_base_model=schema_pydantic_base_model,
            schema_check_type='dict',
        )
        self.agent_name = agent_name

    def process_state(
        self,
        state: AnalysisState,
        config: RunnableConfig,
    ) -> dict:
        chat_histories = self._before_call_analyst(
            chat_history=state.chat_history,
            remaining_retrieve_rounds=state.remaining_retrieve_rounds,
        )
        analysis_result = self.analyze(
            chat_history=chat_histories,
        )
        return dict(

        )

    def get_state_to_be_updated(
        self,
        this_agent_name: Literal['control', 'financial', 'strategic'],
        analyst_chat_history: list[AnyMessage],
        validator_chat_history: list[AnyMessage],
        arbiter_context: list[str],
        remaining_retrieve_rounds: int,
    ) -> dict:
        state_to_be_updated = {}
        response = self.analyze(
            chat_history=analyst_chat_history,
        )
        agent_request = self.get_structured_output(response=response.content)
        # 无论怎么样，记录本次analyst的分析。
        state_to_be_updated[f'{this_agent_name}_analyst_chat_history'] = analyst_chat_history + [response]
        if agent_request['agent_name'] == 'validator':
            # 不需要更多的信息。
            # 控制，去验证。
            state_to_be_updated['current_agent_name'] = 'validator'
            state_to_be_updated['more_information'] = False
            content_to_arbiter = (
                f"<!--{this_agent_name}-analyst-start-->\n\n"
                + response.content
                + f"\n\n<!--{this_agent_name}-analyst-end-->"
            )
            # 将分析提交给validator。
            state_to_be_updated['validator_chat_history'] = validator_chat_history + [
                HumanMessage(content=content_to_arbiter)
            ]
            # 让arbiter看到记录。
            state_to_be_updated['arbiter_context'] = arbiter_context + [content_to_arbiter]
            # 重置可查询次数。
            state_to_be_updated['remaining_retrieve_rounds'] = 5
        else:  # agent_request['agent_name'] == 'document_reader'
            # 需要更多的信息，并且需要指定查询内容。
            # 控制，去对应的document_reader。
            state_to_be_updated['current_agent_name'] = f'{this_agent_name}_document_reader'
            state_to_be_updated['more_information'] = True
            # 说明要查询的内容。
            state_to_be_updated['current_message'] = agent_request['message']
            # 使用一次查询。更新可查询次数-1。
            state_to_be_updated['remaining_retrieve_rounds'] = remaining_retrieve_rounds - 1
        return state_to_be_updated

    def analyze(
        self,
        chat_history: list[AnyMessage],
    ) -> dict:
        # 这里可以直接请求，因为document-reader已经将阅读的结果以HumanMessage写到analyst的chat-history里。
        response = self.call_llm_with_retry(chat_history=chat_history)
        agent_request = self.get_structured_output(raw_str=response.content)
        return dict(
            chat_history=chat_history + [response],
            agent_request=AgentRequest(**agent_request),
        )

    def _before_call_analyst(
        self,
        chat_history: list[AnyMessage],
        remaining_retrieve_rounds: int,
    ) -> list[AnyMessage]:
        if remaining_retrieve_rounds == 0:
            last_round_content = chat_history[-1].content
            last_round_content = last_round_content + "\n\n已经用完这一轮分析的查询次数，这次必须做出小结交给validator进行验证。"
        else:
            last_round_content = chat_history[-1].content
        chat_history[-1] = HumanMessage(content=last_round_content)
        return chat_history

