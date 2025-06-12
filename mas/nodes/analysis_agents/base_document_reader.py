"""
基础的document-reader的定义。
"""

from __future__ import annotations

from ..base_agent import BaseAgent
from mas.utils.human_content_input_processor import HumanContentInputProcessor

from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from mas.schemas.analysis_state import AnalysisState
    from langchain_core.documents import Document
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage


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
        super().__init__(
            chat_prompt_template=chat_prompt_template,
            llm=llm,
            max_retries=10,
            is_need_structured_output=False,
            schema_pydantic_base_model=None,
            schema_check_type='dict',
        )

    def process_state(self, state: AnalysisState) -> dict:
        """
        根据当前的问题，阅读对应的文档。

        Args:
            state: 具体使用参数为current_query和current_query_results。

        Returns:
            更新:
                - 重写query和获得结果的记录。
                - 对应的analyst的chat_history。
        """
        raise NotImplementedError

    # def read_documents(
    #     self,
    #     current_query_results: list[Document],
    #     current_query: str,
    #     document_reader_chat_history: list[AnyMessage],
    # ) -> list[AnyMessage]:
    #     if self.mode == 'text':
    #         return self.read_text_documents(
    #             current_query_results=current_query_results,
    #             current_query=current_query,
    #             document_reader_chat_history=document_reader_chat_history,
    #         )
    #     else:  # self.mode == 'image':
    #         return self.read_image_documents(
    #             current_query_results=current_query_results,
    #             current_query=current_query,
    #             document_reader_chat_history=document_reader_chat_history,
    #         )

    def read_documents(
        self,
        query: str,
        text_documents: list[Document] = None,
        image_documents: list[Document] = None,
    ):
        ...

    def read_text_documents(
        self,
        current_query_results: list[Document],
        current_query: str,
        document_reader_chat_history: list[AnyMessage],
    ) -> list[AnyMessage]:
        text_human_message = self._get_text_human_message(
            documents=current_query_results,
            text_content=current_query,
        )
        chat_history = document_reader_chat_history + [text_human_message]
        response = self.call_llm_with_retry(chat_history=chat_history)
        chat_history = chat_history + [response]
        return chat_history

    def read_image_documents(
        self,
        current_query_results: list[Document],
        current_query: str,
        document_reader_chat_history: list[AnyMessage],
    ) -> list[AnyMessage]:
        image_human_message = self._get_text_human_message(
            documents=current_query_results,
            text_content=current_query,
        )
        chat_history = document_reader_chat_history + [image_human_message]
        response = self.call_llm_with_retry(chat_history=chat_history)
        chat_history = chat_history + [response]
        return chat_history

    @staticmethod
    def text_documents_to_text(
        text_documents: list[Document],
    ) -> str:
        documents_str = '\n\n'.join([text_document.page_content for text_document in text_documents])
        return documents_str
        human_message_content = (
            "从原文件中查找到以下几个相关的文档：\n\n"
            + documents_str
            + f"\n\n{text_content}"
        )
        return HumanMessage(content=human_message_content)

    @staticmethod
    def image_documents_to_content_dict(
        image_documents: list[Document],
    ) -> list[dict]:
        documents_contents = [
            HumanContentInputProcessor.get_image_content_dict_from_base64(base64_str=image_document.page_content)
            for image_document in image_documents
        ]
        return documents_contents
        query_content_dict = HumanContentInputProcessor.get_text_content_dict(text=text_content)
        human_message_content = documents_contents + [query_content_dict]
        return HumanMessage(content=human_message_content)

