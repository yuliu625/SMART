"""

"""

from .decision_agents import (
    Recognizer,
    Validator,
    Arbiter,
)
from mas.graph.prompts import PromptTemplateFactory
from mas.models import LLMFactory

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate


class AgentFactory:
    """

    """
    def __init__(self):
        self.prompt_template_factory = PromptTemplateFactory()
        self.llm_factory = LLMFactory()

    def get_rag_agent(self):
        rag_system_message = self.prompt_template_factory.get_system_message(agent_name='rag')
        rag_with_system_prompt_template = self._get_with_system_prompt_template(
            system_message=rag_system_message,
        )
        return rag_with_system_prompt_template

    def get_recognizer(self):
        recognizer_system_message = self.prompt_template_factory.get_system_message(agent_name='recognizer')
        recognizer_with_system_prompt_template = self._get_with_system_prompt_template(
            system_message=recognizer_system_message
        )
        recognizer = Recognizer(llm_chain=recognizer_with_system_prompt_template)
        return recognizer

    def get_validator(self):
        validator_system_message = self.prompt_template_factory.get_system_message(agent_name='validator')
        validator_with_system_prompt_template = self._get_with_system_prompt_template(
            system_message=validator_system_message
        )
        validator = Validator(llm_chain=validator_with_system_prompt_template)
        return validator

    def get_arbiter(self):
        arbiter_system_message = self.prompt_template_factory.get_system_message(agent_name='arbiter')
        arbiter_with_system_prompt_template = self._get_with_system_prompt_template(
            system_message=arbiter_system_message
        )
        arbiter = Arbiter(llm_chain=arbiter_with_system_prompt_template)
        return arbiter

    def _get_with_system_prompt_template(
        self,
        system_message: SystemMessage,
    ) -> ChatPromptTemplate:
        chat_prompt_template = ChatPromptTemplate.from_messages([
            system_message,
            MessagesPlaceholder('chat_history'),
        ])
        return chat_prompt_template

