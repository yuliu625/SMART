"""

"""

from mas.global_config import LLM_MAS_RETRIES
from ...states import MASState
from ...prompts import PromptTemplateFactory
from mas.utils import JsonOutputParser
from mas.models import LLMFactory
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage, AnyMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.vectorstores import VectorStore, VectorStoreRetriever
from langchain_core.documents import Document


class MultiQueryRetriever:
    """

    """
    def __init__(
        self,
        retriever: VectorStoreRetriever,
    ):
        self.retriever = retriever

        self._llm_factory = LLMFactory()
        self._llm = self._llm_factory.get_qwen_llm('qwen-plus')

        self._prompt_template_factory = PromptTemplateFactory()
        self.llm_chain = self._get_llm_chain()

    def run(self, state: MASState):
        query_chat_history = self.process_query_chat_history(
            current_query=state.current_query,
            last_round_result_number=state.last_round_result_number,
            query_chat_history=state.query_chat_history,
        )
        # call llm，获得重写的query
        rewrite_queries = self.get_rewrite_queries(query_chat_history=query_chat_history)
        # 更新查询聊天历史
        query_chat_history += rewrite_queries['response']
        # 获得重写的查询
        queries = rewrite_queries['queries']
        # 获得原始查询结果
        query_result = self.batch_retrieve(queries=queries)
        # 处理查询结果
        processed_result = self.get_unique_results(
            current_query_results=query_result,
            query_result_history=state.query_result_history,
        )
        current_query_results = processed_result['current_query_results']
        query_result_history = processed_result['query_result_history']
        # 更新状态
        return {
            'query_chat_history': query_chat_history,
            'query_result_history': query_result_history,
            'last_round_result_number': len(current_query_results),
            'current_query_results': current_query_results,
        }

    def process_query_chat_history(
        self,
        current_query: str,
        last_round_result_number: int,
        query_chat_history: list,
    ):
        if last_round_result_number == -1:
            # 这是初始第一轮
            query_chat_history.append(HumanMessage(content=current_query))
        else:
            query_chat_history.append(
                HumanMessage(
                    content=f"在上一轮，我根据你改写的查询获得了{last_round_result_number}条结果。\n这轮，我需要查询的问题是：\n{current_query}"
                )
            )
        return query_chat_history

    def get_rewrite_queries(self, query_chat_history: list[AnyMessage]) -> dict:
        queries = ['']
        for i in range(LLM_MAS_RETRIES):
            response = self.llm_chain.invoke({'chat_history': query_chat_history})
            queries = JsonOutputParser.extract_json_from_str(response.content)
            if queries:
                break
        return {
            'response': response,
            'queries': queries,
        }

    def batch_retrieve(
        self,
        queries: list[str]
    ) -> list[Document]:
        results = []
        for query in queries:
            result = self.retriever.invoke(query)
            results += result
        unique_documents_ids = set()
        unique_documents = []
        for document in results:
            if document.id not in unique_documents_ids:
                unique_documents_ids.add(document.id)
                unique_documents.append(document)
        return unique_documents

    def get_unique_results(
        self,
        current_query_results: list[Document],
        query_result_history: list[Document],
    ) -> dict:
        # 去重。
        # 过去查询以及有的文档
        history_document_ids = [document.id for document in query_result_history]
        result = []
        for query_result in current_query_results:  # 在过去的查询结果中
            if query_result.id not in history_document_ids:  # 如果当前的文档的id在历史中没有
                result.append(query_result)  # 添加至最终的结果。
        query_result_history = query_result_history + result
        return {
            'current_query_results': result,  # 更新去重后当前的查询结果。
            'query_result_history': query_result_history  # 将当前结果添加到历史中。
        }

    def _get_llm_chain(self):
        system_message = self._prompt_template_factory.get_system_message('rag')
        with_system_prompt_template = self._get_with_system_prompt_template(system_message=system_message)
        chain = with_system_prompt_template | self._llm
        return chain

    def _get_with_system_prompt_template(
        self,
        system_message: SystemMessage,
    ) -> ChatPromptTemplate:
        chat_prompt_template = ChatPromptTemplate.from_messages([
            system_message,
            MessagesPlaceholder('chat_history'),
        ])
        return chat_prompt_template

