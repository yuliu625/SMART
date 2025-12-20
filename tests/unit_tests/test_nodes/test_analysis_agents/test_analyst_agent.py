"""

"""

from __future__ import annotations
import pytest

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from mas.agent_nodes import AgentFactory

from langchain_core.messages import HumanMessage


def test_analyst_1():
    agent_factory = AgentFactory()
    llm_chain = agent_factory._get_llm_chain(llm_name='qwen-plus', agent_name='analyst')
    chat_history = [
        HumanMessage(content=(
            "<!--document-reader-->"
            "从原文件中查找到以下几个相关的文档：\n\n"
            "##利润\nA公司在过去一年的净利润是50万元\n\n"
            "问题：A公司的盈利状况"
        ))
    ]
    response = llm_chain.invoke({'chat_history': chat_history})
    print(response)


if __name__ == '__main__':
    test_analyst_1()
