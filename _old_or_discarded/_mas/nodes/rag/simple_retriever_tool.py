"""

"""

from langchain.tools.retriever import create_retriever_tool

from langchain_core.retrievers import BaseRetriever


def get_simple_text_retriever_tool(
    retriever: BaseRetriever,
):
    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name='simple_text_rag',
        description=""
    )
    return retriever_tool


def get_simple_image_retriever_tool(
    retriever: BaseRetriever,
):
    retriever_tool = create_retriever_tool(
        retriever=retriever,
        name='simple_image_rag',
        description=""
    )
    return retriever_tool

