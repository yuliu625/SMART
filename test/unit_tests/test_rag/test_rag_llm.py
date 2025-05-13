"""

"""

from mas.models import LLMFactory
from mas.graph.prompts import PromptTemplateFactory

from langchain_core.messages import HumanMessage


def test_rag_llm():
    llm_factory = LLMFactory()
    llm = llm_factory.get_qwen_llm('qwen-plus')
    prompt_template_factory = PromptTemplateFactory()
    rag_system_message = prompt_template_factory.get_system_message(agent_name='rag')
    response = llm.invoke([
        rag_system_message,
        HumanMessage("我需要查看公司的现金流量。"),
    ])
    print(response)


if __name__ == '__main__':
    test_rag_llm()
