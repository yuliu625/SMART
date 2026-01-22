"""
构建各个作为agent的node。
"""

from __future__ import annotations
from loguru import logger

from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.investigator import Investigator
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
from mas.agent_nodes.analysis_agents.analyst import Analyst

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from mas.agent_nodes.base_agent import BaseAgent
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, AIMessage, SystemMessage
    from pydantic import BaseModel


class AgentFactory:
    @staticmethod
    def create_agent(
        agent_type: Literal[
            'surveyor', 'investigator', 'adjudicator',
            'analyst', 'rag_agent',
        ],
    ) -> BaseAgent:
        raise NotImplementedError

    @staticmethod
    def create_surveyor(
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
    ) -> BaseAgent:
        surveyor = Surveyor(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
        )
        return surveyor

    @staticmethod
    def create_investigator(
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ) -> BaseAgent:
        investigator = Investigator(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            formatter_llm=formatter_llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
            formatter_llm_system_message=formatter_llm_system_message,
        )
        return investigator

    @staticmethod
    def create_adjudicator(
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ) -> BaseAgent:
        adjudicator = Adjudicator(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            formatter_llm=formatter_llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
            formatter_llm_system_message=formatter_llm_system_message,
        )
        return adjudicator

    @staticmethod
    def create_analyst(
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ) -> BaseAgent:
        analyst = Analyst(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            formatter_llm=formatter_llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
            formatter_llm_system_message=formatter_llm_system_message,
        )
        return analyst

    @staticmethod
    def create_rag_agent(

    ) -> BaseAgent:
        raise NotImplementedError

