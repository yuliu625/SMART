"""

"""

from ...states import MASState
from ..base_agent import BaseAgent
from mas.utils import get_image_content_dict_from_base64, get_text_content

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, AnyMessage

from langchain_core.runnables import Runnable
from langchain_core.documents import Document
from pydantic import BaseModel
from typing import Literal


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
        llm_chain: Runnable,
        mode: Literal['text', 'image'] = 'image',
    ):
        super().__init__(
            llm_chain=llm_chain,
        )
        self.llm_chain = llm_chain
        self.mode = mode

    def run(self, state: MASState):
        """
        根据当前的问题，阅读对应的文档。

        Args:
            state: 具体使用参数为current_query和current_query_results。

        Returns:
            更新:
                - 重写query和获得结果的记录。
                - 对应的analyst的chat_history。
        """
        chat_history = self.read_documents(state=state)
        return {
            'document_reader_history': chat_history,
            # 'analyst_chat_history': ,
        }

    def read_documents(self, state: MASState) -> list[AnyMessage]:
        if self.mode == 'text':
            return self.read_text_documents(state)
        else:  # self.mode == 'image':
            return self.read_image_documents(state)

    def read_text_documents(self, state: MASState) -> list[AnyMessage]:
        text_human_message = self._get_text_human_message(
            documents=state.current_query_results,
            text_content=state.current_query,
        )
        chat_history = state.document_reader_history + [text_human_message]
        response = self.call_llm_chain(chat_history=chat_history)
        chat_history = chat_history + [response]
        return chat_history

    def read_image_documents(self, state: MASState) -> list[AnyMessage]:
        image_human_message = self._get_text_human_message(
            documents=state.current_query_results,
            text_content=state.current_query,
        )
        chat_history = state.document_reader_history + [image_human_message]
        response = self.call_llm_chain(chat_history=chat_history)
        chat_history = chat_history + [response]
        return chat_history

    def _get_text_human_message(
        self,
        documents: list[Document],
        text_content: str,
    ) -> HumanMessage:
        documents_str = '\n\n'.join([document.page_content for document in documents])
        human_message_content = (
            "从原文件中查找到以下几个相关的文档：\n\n"
            + documents_str
            + f"\n\n{text_content}"
        )
        return HumanMessage(content=human_message_content)

    def _get_image_human_message(
        self,
        documents: list[Document],
        text_content: str,
    ) -> HumanMessage:
        documents_contents = [
            get_image_content_dict_from_base64(base64_str=document.page_content)
            for document in documents
        ]
        query_content_dict = get_text_content(text=text_content)
        human_message_content = documents_contents + [query_content_dict]
        return HumanMessage(content=human_message_content)

