"""

"""

from mas.graph.nodes.base_agent import BaseAgent
from mas.models import LLMFactory

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage


def test_base_agent_1():
    llm_chain = ChatPromptTemplate.from_messages([
        SystemMessage("你是AI。"),
        MessagesPlaceholder('chat_history'),
    ])
    agent = BaseAgent(
        llm_chain=llm_chain,
    )
    response = agent.call_llm_chain([
        HumanMessage("喂喂喂")
    ])
    print(response)


def test_base_agent_2():
    llm_factory = LLMFactory()
    llm = llm_factory.get_qwen_llm('qwen-plus')
    chat_prompt_template = ChatPromptTemplate.from_messages([
        SystemMessage("你仅以markdown包裹的JSON格式回答问题。"),
        MessagesPlaceholder('chat_history'),
    ])
    agent = BaseAgent(
        llm_chain=chat_prompt_template | llm,
    )
    response = agent.call_llm_chain([
        HumanMessage("给我一个1-3的数组。")
    ])
    print(response)


if __name__ == '__main__':
    test_base_agent_1()
    test_base_agent_2()
