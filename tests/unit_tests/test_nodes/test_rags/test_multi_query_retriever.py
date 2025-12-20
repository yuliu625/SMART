"""

"""

from __future__ import annotations
import pytest

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from mas.schemas import MASState
from mas.utils import VectorStoreLoader
from mas.agent_nodes import RagRetrieverFactory


def test_multi_query_retriever_1():
    vector_store_loader = VectorStoreLoader(base_dir=r'D:\dataset\risk_mas_t')
    vector_store = vector_store_loader.get_vector_store('text', 'rule', 'fake')
    rag_retriever_factory = RagRetrieverFactory(vector_store=vector_store, pdf_name='1910.13461v1.pdf')
    financial_retriever = rag_retriever_factory.get_control_multi_query_retriever()
    result = financial_retriever.run(MASState(current_message='bart'))
    print(result)


def test_multi_query_retriever_2():
    vector_store_loader = VectorStoreLoader(base_dir=r'D:\dataset\risk_mas_t')
    vector_store = vector_store_loader.get_vector_store('text', 'rule', 'fake')
    rag_retriever_factory = RagRetrieverFactory(vector_store=vector_store, pdf_name='1910.13461v1.pdf')
    financial_retriever = rag_retriever_factory.get_financial_multi_query_retriever()
    result = financial_retriever.run(MASState(current_message='bart'))
    print(result)


def test_multi_query_retriever_3():
    vector_store_loader = VectorStoreLoader(base_dir=r'D:\dataset\risk_mas_t')
    vector_store = vector_store_loader.get_vector_store('text', 'rule', 'fake')
    rag_retriever_factory = RagRetrieverFactory(vector_store=vector_store, pdf_name='1910.13461v1.pdf')
    financial_retriever = rag_retriever_factory.get_strategic_multi_query_retriever()
    result = financial_retriever.run(MASState(current_message='bart'))
    print(result)


if __name__ == '__main__':
    test_multi_query_retriever_1()
    test_multi_query_retriever_2()
    test_multi_query_retriever_3()
