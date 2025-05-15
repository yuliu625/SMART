"""

"""

from .base_document_reader import BaseDocumentReader
from ...states import MASState

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage, AnyMessage

from langchain_core.runnables import Runnable
from typing import Literal


class FinancialDocumentReader(BaseDocumentReader):
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
        financial_document_reader_chat_history = self.read_documents(
            current_query=state.current_message,
            current_query_results=state.financial_current_query_results,
            document_reader_chat_history=state.financial_document_reader_chat_history,
        )
        financial_analyst_chat_history = state.financial_analyst_chat_history + [HumanMessage(
            content=financial_document_reader_chat_history[-1].content,
        )]
        return {
            'financial_document_reader_chat_history': financial_document_reader_chat_history,
            'financial_analyst_chat_history': financial_analyst_chat_history,
        }

