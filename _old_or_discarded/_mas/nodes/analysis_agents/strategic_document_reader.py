"""

"""

from .base_document_reader import BaseDocumentReader
from mas.schemas import MASState

from langchain_core.messages import HumanMessage

from langchain_core.runnables import Runnable
from typing import Literal


class StrategicDocumentReader(BaseDocumentReader):
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
        strategic_document_reader_chat_history = self.read_documents(
            current_query=state.current_message,
            current_query_results=state.strategic_current_query_results,
            document_reader_chat_history=state.strategic_document_reader_chat_history
        )
        strategic_analyst_chat_history = state.strategic_analyst_chat_history + [HumanMessage(
            content=strategic_document_reader_chat_history[-1].content,
        )]
        return {
            'strategic_document_reader_chat_history': strategic_document_reader_chat_history,
            'strategic_analyst_chat_history': strategic_analyst_chat_history,
        }

