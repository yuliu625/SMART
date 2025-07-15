"""

"""

from .base_document_reader import BaseDocumentReader
from mas.schemas import MASState

from langchain_core.messages import HumanMessage

from langchain_core.runnables import Runnable
from typing import Literal


class ControlDocumentReader(BaseDocumentReader):
    def __init__(
        self,
        llm_chain: Runnable,
        mode: Literal['text', 'image'] = 'image',
    ):
        super().__init__(
            llm_chain=llm_chain,
            mode=mode,
        )

    def run(self, state: MASState):
        control_document_reader_chat_history = self.read_documents(
            current_query=state.current_message,
            current_query_results=state.control_current_query_results,
            document_reader_chat_history=state.control_document_reader_chat_history,
        )
        control_analyst_chat_history = state.control_analyst_chat_history + [HumanMessage(
            content=control_document_reader_chat_history[-1].content,
        )]
        return {
            'control_document_reader_chat_history': control_document_reader_chat_history,
            'control_analyst_chat_history': control_analyst_chat_history,
        }

