

from mas.graph.prompts import PromptTemplateFactory
from mas.models import LLMFactory

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate


class AgentFactory:
    def __init__(self):
        self.prompt_template_factory = PromptTemplateFactory()

    def get_recognizer(self):
        ...

