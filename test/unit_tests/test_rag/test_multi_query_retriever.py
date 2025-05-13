"""

"""

from mas.graph.states import MASState
from mas.utils import VectorStoreLoader
from mas.graph.nodes import RagRetrieverFactory


def test_multi_query_retriever():
    vector_store_loader = VectorStoreLoader(base_dir=r'D:\dataset\risk_mas_t')
    vector_store = vector_store_loader.get_vector_store('text', 'rule', 'model1')
    rag_retriever_factory = RagRetrieverFactory(vector_store=vector_store, pdf_name='1910.13461v1.pdf')
    retriever = rag_retriever_factory.get_multi_query_retriever()
    retriever.run()


if __name__ == '__main__':
    test_multi_query_retriever()
