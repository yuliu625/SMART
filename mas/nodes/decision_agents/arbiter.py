"""
仲裁者。
"""

from __future__ import annotations

from mas.nodes.base_agent import BaseAgent
from mas.schemas.structured_output_format import ArbiterDecision
from mas.utils.content_annotator import ContentAnnotator

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.decision_state import DecisionState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.messages import AnyMessage


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
            is_need_structured_output=True,
            schema_pydantic_base_model=ArbiterDecision,
            schema_check_type='dict',
        )

    def process_state(
        self,
        state: DecisionState,
        config: RunnableConfig,
    ) -> dict:
        arbiter_result = self.arbitrate(
            shared_chat_history=state.shared_chat_history,
        )
        return dict(

        )

    def arbitrate(
        self,
        shared_chat_history: list[AnyMessage],
    ) -> dict:
        # 合并所有的讨论记录。
        merged_content = self.merge_chat_history(chat_history=shared_chat_history)
        # 获取llm响应。
        response = self.call_llm_with_retry(chat_history=[HumanMessage(content=merged_content)])
        # 提取最终结论。
        arbiter_decision = self.get_structured_output(raw_str=response.content)
        return dict(
            shared_chat_history=shared_chat_history + [response],
            arbiter_decision=arbiter_decision,
        )

    def merge_chat_history(
        self,
        chat_history: list[AnyMessage],
    ) -> str:
        merged_content = ""  # '\n\n'.join(message.content for message in chat_history)
        for message in chat_history:
            if isinstance(message, AIMessage):
                merged_content += ContentAnnotator.annotate_with_html_comment(
                    tag='validator',
                    original_text=message.content,
                )
            else:
                merged_content += message.content
            merged_content += '\n\n'
        return merged_content

