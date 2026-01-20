"""
构建各种graph的工厂。
"""

from __future__ import annotations
from loguru import logger

# Agent
from mas.agent_nodes.agent_factory import AgentFactory
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.investigator import Investigator
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
# single agent mas
from mas.graphs.single_agent_mas_graph_builder import SingleAgentMASGraphBuilder
from mas.schemas.single_agent_mas_state import SingleAgentMASState
# sequential mas
# multi agent debate
# final mas

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage
    from pydantic import BaseModel


class GraphFactory:
    @staticmethod
    def create_single_agent_mas_graph(
        adjudicator_main_llm: BaseChatModel,
        adjudicator_main_llm_system_message: SystemMessage,
        adjudicator_formatter_llm: BaseChatModel,
        adjudicator_formatter_llm_system_message: SystemMessage,
        adjudicator_structured_output_format: type[BaseModel],
    ) -> CompiledStateGraph:
        graph_builder = SingleAgentMASGraphBuilder(state=SingleAgentMASState)
        adjudicator = AgentFactory.create_adjudicator(
            main_llm=adjudicator_main_llm,
            main_llm_system_message=adjudicator_main_llm_system_message,
            formatter_llm=adjudicator_formatter_llm,
            schema_pydantic_base_model=adjudicator_structured_output_format,
            formatter_llm_system_message=adjudicator_formatter_llm_system_message,
        )
        assert isinstance(adjudicator, Adjudicator)
        graph = graph_builder.build_graph(
            adjudicator=adjudicator,
        )
        return graph

    @staticmethod
    def create_sequential_mas_graph(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_multi_agent_debate_mas_graph(

    ) -> CompiledStateGraph:
        raise NotImplementedError

    @staticmethod
    def create_final_mas_graph(

    ) -> CompiledStateGraph:
        raise NotImplementedError

