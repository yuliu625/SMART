"""

"""

from .analysis_agents import (
    BaseDocumentReader,
    BaseAnalyst,
    ControlAnalyst,
    ControlDocumentReader,
    FinancialAnalyst,
    FinancialDocumentReader,
    StrategicAnalyst,
    StrategicDocumentReader,
)
from .decision_agents import (
    Recognizer,
    Validator,
    Arbiter,
)
from ..states.structured_output_format import (
    RequestAgent,
    ArbiterDecision,
)
from mas.graph.prompts import PromptTemplateFactory
from mas.models import LLMFactory, VLMFactory


from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.prompts import PromptTemplate, MessagesPlaceholder, ChatPromptTemplate


class AgentFactory:
    """
    生成graph中可以使用的node。

    如果进行测试，使用策略模式封装的_get_llm_chain方法。
    """
    def __init__(self):
        self.prompt_template_factory = PromptTemplateFactory()
        self.llm_factory = LLMFactory()
        self.vlm_factory = VLMFactory()

    def _get_document_reader(self):
        document_llm_chain = self._get_llm_chain(llm_name='qwen-vl-max', agent_name='document_reader')
        document_reader = BaseDocumentReader(
            llm_chain=document_llm_chain,
        )
        return document_reader

    def _get_analyst(self):
        analyst_llm_chain = self._get_llm_chain(llm_name='qwen-max', agent_name='analyst')
        analyst = BaseAnalyst(
            llm_chain=analyst_llm_chain,
            structured_output_format=RequestAgent,
        )
        return analyst

    def get_recognizer(self):
        recognizer_llm_chain = self._get_llm_chain(llm_name='qwen-long', agent_name='recognizer')
        recognizer = Recognizer(
            llm_chain=recognizer_llm_chain,
        )
        return recognizer

    def get_validator(self):
        validator_llm_chain = self._get_llm_chain(llm_name='qwen-max', agent_name='validator')
        validator = Validator(
            llm_chain=validator_llm_chain,
            structured_output_format=RequestAgent,
        )
        return validator

    def get_arbiter(self):
        arbiter_llm_chain = self._get_llm_chain(llm_name='qwen-max', agent_name='arbiter')
        arbiter = Arbiter(
            llm_chain=arbiter_llm_chain,
            structured_output_format=ArbiterDecision,
        )
        return arbiter

    def get_control_document_reader(self):
        control_document_reader_llm_chain = self._get_vlm_chain(
            vlm_name='qwen-vl-max', agent_name='control_document_reader'
        )
        control_document_reader = ControlDocumentReader(
            llm_chain=control_document_reader_llm_chain,
        )
        return control_document_reader

    def get_control_analyst(self):
        control_analyst_llm_chain = self._get_llm_chain(llm_name='qwen-max', agent_name='control_analyst')
        control_analyst = ControlAnalyst(
            llm_chain=control_analyst_llm_chain,
            structured_output_format=RequestAgent,
        )
        return control_analyst

    def get_financial_document_reader(self):
        financial_document_reader_llm_chain = self._get_vlm_chain(
            vlm_name='qwen-vl-max', agent_name='financial_document_reader'
        )
        financial_document_reader = FinancialDocumentReader(
            llm_chain=financial_document_reader_llm_chain,
        )
        return financial_document_reader

    def get_financial_analyst(self):
        financial_analyst_llm_chain = self._get_llm_chain(llm_name='qwen-max', agent_name='financial_analyst')
        financial_analyst = FinancialAnalyst(
            llm_chain=financial_analyst_llm_chain,
            structured_output_format=RequestAgent,
        )
        return financial_analyst

    def get_strategic_document_reader(self):
        strategic_document_reader_llm_chain = self._get_vlm_chain(
            vlm_name='qwen-vl-max', agent_name='strategic_document_reader'
        )
        strategic_document_reader = StrategicDocumentReader(
            llm_chain=strategic_document_reader_llm_chain,
        )
        return strategic_document_reader

    def get_strategic_analyst(self):
        strategic_analyst_llm_chain = self._get_llm_chain(llm_name='qwen-max', agent_name='strategic_analyst')
        strategic_analyst = StrategicAnalyst(
            llm_chain=strategic_analyst_llm_chain,
            structured_output_format=RequestAgent,
        )
        return strategic_analyst

    def _get_llm_chain(
        self,
        llm_name: str,
        agent_name: str,
    ):
        system_message = self.prompt_template_factory.get_system_message(agent_name=agent_name)
        with_system_prompt_template = self._get_with_system_prompt_template(
            system_message=system_message,
        )
        llm = self.llm_factory.get_qwen_llm(model=llm_name)
        llm_chain = with_system_prompt_template | llm
        return llm_chain

    def _get_vlm_chain(
        self,
        vlm_name: str,
        agent_name: str,
    ):
        system_message = self.prompt_template_factory.get_system_message(agent_name=agent_name)
        with_system_prompt_template = self._get_with_system_prompt_template(
            system_message=system_message,
        )
        llm = self.vlm_factory.get_qwen_vlm(model=vlm_name)
        llm_chain = with_system_prompt_template | llm
        return llm_chain

    def _get_with_system_prompt_template(
        self,
        system_message: SystemMessage,
    ) -> ChatPromptTemplate:
        chat_prompt_template = ChatPromptTemplate.from_messages([
            system_message,
            MessagesPlaceholder('chat_history'),
        ])
        return chat_prompt_template

