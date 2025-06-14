"""
基础的document-reader的定义。
"""

from __future__ import annotations

from mas.nodes.base_agent import BaseAgent
from mas.utils.human_content_input_processor import HumanContentInputProcessor

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from mas.schemas.analysis_state import AnalysisState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.documents import Document
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, AIMessage


class BaseDocumentReader(BaseAgent):
    """
    基础文档阅读者。

    文档阅读者都是VLM，根据问题提取有用的信息。
    为了更加全面的信息和降低任务复杂度，文档阅读者不需要结构化输出。

    派生类需要重写:
        - run: 指明状态更新的字段。
        - read_text_documents: 指明使用的文档和查询的字段。
        - read_image_documents: 指明使用的文档和查询的字段。
    """
    def __init__(
        self,
        chat_prompt_template: ChatPromptTemplate,
        llm: BaseChatModel,
    ):
        """
        文档阅读者，完全不做任何限制的LLM。
        """
        super().__init__(
            chat_prompt_template=chat_prompt_template,
            llm=llm,
            max_retries=10,
            is_need_structured_output=False,
            schema_pydantic_base_model=None,
            schema_check_type='dict',
        )

    def process_state(
        self,
        state: AnalysisState,
        config: RunnableConfig,
    ) -> dict:
        """
        根据当前的问题，阅读对应的文档。

        Args:
            state: 具体使用参数为current_query和current_query_results。
            config:

        Returns:
            更新:
                - 重写query和获得结果的记录。
                - 对应的analyst的chat_history。
        """
        raise NotImplementedError

    def read_multimodal_documents(
        self,
        chat_history: list[AnyMessage],
        query: str,
        text_documents: list[Document] = None,
        image_documents: list[Document] = None,
    ) -> AIMessage:

        response = self.call_llm_with_retry(chat_history=chat_history)
        return response

    def read_text_documents(
        self,
        chat_history: list[AnyMessage],
        query: str,
        text_documents: list[Document],
    ) -> list[AnyMessage]:
        chat_history_ = chat_history.copy()
        text = self.text_documents_to_str(text_documents=text_documents)
        human_message_content = self.wrap_message_content_with_agent_name(
            agent_name='text-document',
            original_content=text,
        )
        chat_history_ = chat_history_ + [HumanMessage(
            content=human_message_content,
        )]
        response = self.call_llm_with_retry(chat_history=chat_history_)
        chat_history_ = chat_history_ + [response]
        return chat_history_

    def get_human_message(
        self,
    ):
        ...

    def read_image_documents(
        self,
        chat_history: list[AnyMessage],
        query: str,
        image_documents: list[Document],
    ) -> list[AnyMessage]:
        chat_history_ = chat_history.copy()
        image_content_dicts = self.image_documents_to_content_dicts(image_documents=image_documents)
        human_message_content = image_content_dicts + [HumanContentInputProcessor.get_text_content_dict(text=query)]
        chat_history_ = chat_history_ + [HumanMessage(
            content=human_message_content,
        )]
        response = self.call_llm_with_retry(chat_history=chat_history_)
        chat_history_ = chat_history_ + [response]
        return chat_history_

    @staticmethod
    def text_documents_to_str(
        text_documents: list[Document],
    ) -> str:
        documents_str = '\n\n'.join([text_document.page_content for text_document in text_documents])
        human_message_content = (
            "从原文件中查找到以下几个相关的文本片段: \n\n"
            + documents_str
            + '\n\n'
        )
        return human_message_content

    @staticmethod
    def image_documents_to_content_dicts(
        image_documents: list[Document],
    ) -> list[dict]:
        image_documents_contents = [
            HumanContentInputProcessor.get_image_content_dict_from_base64(base64_str=image_document.page_content)
            for image_document in image_documents
        ]
        return image_documents_contents
        # query_content_dict = HumanContentInputProcessor.get_text_content_dict(text=text_content)
        # human_message_content = documents_contents + [query_content_dict]
        # return HumanMessage(content=human_message_content)

