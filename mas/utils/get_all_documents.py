"""

"""

from langchain_core.vectorstores import VectorStore


def get_all_documents(
    vector_store: VectorStore,
):
    # 方法: 以空字符串，查询远超过存储容量的记录，这样就能返回全部的记录。
    documents = vector_store.similarity_search('', k=100000000)
    return documents

