"""

"""

from mas.graph.nodes import AgentFactory
from mas.utils import get_text_content, get_image_content_dict_from_base64
from mas.utils.base64_to_pil import uri_to_base64

from langchain_core.messages import AIMessage, HumanMessage


def test_document_reader_1():
    agent_factory = AgentFactory()
    llm_chain = agent_factory._get_llm_chain(llm_name='qwen-plus', agent_name='document_reader')
    chat_history = [
        HumanMessage(content=(
            "从原文件中查找到以下几个相关的文档：\n\n"
            "##利润\nA公司在过去一年的净利润是50万元\n\n"
            "问题：A公司的盈利状况"
        ))
    ]
    response = llm_chain.invoke({'chat_history': chat_history})
    print(response)


def test_document_reader_2():
    agent_factory = AgentFactory()
    llm_chain = agent_factory._get_llm_chain(llm_name='qwen-vl-max', agent_name='document_reader')
    chat_history = [
        HumanMessage(content=(
            "从原文件中查找到以下几个相关的文档：\n\n"
            "##利润\nA公司在过去一年的净利润是50万元\n\n"
            "问题：A公司的盈利状况"
        ))
    ]
    response = llm_chain.invoke({'chat_history': chat_history})
    print(response)


def test_document_reader_3():
    agent_factory = AgentFactory()
    llm_chain = agent_factory._get_llm_chain(llm_name='qwen-vl-max', agent_name='document_reader')
    chat_history = [
        HumanMessage(content=[
            get_image_content_dict_from_base64(uri_to_base64(r"D:\dataset\risk_mas_t\image_pdf\1910.13461v1.pdf\page_1.png")),
            get_text_content("bart基本介绍")
        ])
    ]
    response = llm_chain.invoke({'chat_history': chat_history})
    print(response)


if __name__ == '__main__':
    # test_document_reader_1()
    # test_document_reader_2()
    test_document_reader_3()
