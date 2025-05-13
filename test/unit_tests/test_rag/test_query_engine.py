"""

"""

from mas.graph.nodes.rag import RagRetrieverFactory
from mas.models import LLMFactory
from mas.utils import VectorStoreLoader


def test_simple_retriever():
    vector_store_loader = VectorStoreLoader(base_dir=r'D:\dataset\risk_mas_t')
    vector_store = vector_store_loader.get_vector_store('text', 'rule', 'model1')
    rag_retriever_factory = RagRetrieverFactory(vector_store=vector_store, pdf_name='1910.13461v1.pdf')
    query_engine = rag_retriever_factory.get_simple_retriever()
    response = query_engine.invoke('bart')
    print(len(response))
    print(response)


def test_query_engine():
    rag_retriever_factory = RagRetrieverFactory()
    llm_factory = LLMFactory()
    llm = llm_factory.get_qwen_llm('qwen-plus')
    vector_store_loader = VectorStoreLoader(base_dir=r'D:\dataset\risk_mas_t')
    vector_store = vector_store_loader.get_vector_store('text', 'rule', 'model1')
    query_engine = rag_retriever_factory.get_multi_query_retriever(
        vector_store=vector_store,
        llm=llm,
    )
    response = query_engine.invoke({'question': 'bart'})
    print(len(response))
    print(response)


if __name__ == '__main__':
    test_simple_retriever()
    # test_query_engine()
