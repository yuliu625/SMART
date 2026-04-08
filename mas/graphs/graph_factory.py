"""
构建各种graph的工厂。
"""

from __future__ import annotations
from loguru import logger

# Agent
from mas.agent_nodes.agent_factory import AgentFactory
## Decision Agents
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.investigator import Investigator
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
## Analysis Agents
from mas.agent_nodes.analysis_agents.analyst import Analyst
from mas.agent_nodes.analysis_agents.proponent import Proponent
from mas.agent_nodes.analysis_agents.opponent import Opponent
# RAG
# from mas.rag_nodes.chroma_rag_builder import ChromaRAGBuilder
# from mas.rag_nodes.qdrant_rag_builder import QdrantRAGBuilder
# MAS
## Single Agent
from mas.graphs.single_agent_graph_builder import SingleAgentGraphBuilder
from mas.schemas.single_agent_state import SingleAgentState
## Sequential Workflow
from mas.graphs.sequential_workflow_graph_builder import SequentialWorkflowGraphBuilder
from mas.schemas.sequential_workflow_state import SequentialWorkflowState
## Multi-Agent Debate
from mas.graphs.multi_agent_debate_graph_builder import MultiAgentDebateGraphBuilder
from mas.schemas.multi_agent_debate_state import MultiAgentDebateState
## final MAS
from mas.graphs.final_mas_graph_builder import FinalMASGraphBuilder
from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING, cast
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import SystemMessage
    from pydantic import BaseModel


class GraphFactory:
    @staticmethod
    def create_single_agent_graph(
        adjudicator_main_llm: BaseChatModel,
        adjudicator_main_llm_system_message: SystemMessage,
        adjudicator_formatter_llm: BaseChatModel,
        adjudicator_formatter_llm_system_message: SystemMessage,
        adjudicator_structured_output_format: type[BaseModel],
    ) -> CompiledStateGraph:
        graph_builder = SingleAgentGraphBuilder(state=SingleAgentState)
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
    def create_sequential_workflow_graph(
        # Surveyor
        surveyor_main_llm: BaseChatModel,
        surveyor_main_llm_system_message: SystemMessage,
        # Adjudicator
        adjudicator_main_llm: BaseChatModel,
        adjudicator_main_llm_system_message: SystemMessage,
        adjudicator_formatter_llm: BaseChatModel,
        adjudicator_formatter_llm_system_message: SystemMessage,
        adjudicator_structured_output_format: type[BaseModel],
        # Analyst
        # RAG
        rag,
    ) -> CompiledStateGraph:
        graph_builder = SequentialWorkflowGraphBuilder(state=SequentialWorkflowState)
        # Surveyor
        surveyor = AgentFactory.create_surveyor(
            main_llm=surveyor_main_llm,
            main_llm_system_message=surveyor_main_llm_system_message,
        )
        assert isinstance(surveyor, Surveyor)
        # Adjudicator
        adjudicator = AgentFactory.create_adjudicator(
            main_llm=adjudicator_main_llm,
            main_llm_system_message=adjudicator_main_llm_system_message,
            formatter_llm=adjudicator_formatter_llm,
            schema_pydantic_base_model=adjudicator_structured_output_format,
            formatter_llm_system_message=adjudicator_formatter_llm_system_message,
        )
        assert isinstance(adjudicator, Adjudicator)
        analyst = AgentFactory.create_information_merger()
        analyst = cast(Analyst, analyst)
        graph = graph_builder.build_graph(
            surveyor=surveyor,
            adjudicator=adjudicator,
            analyst=analyst,
            rag=rag,
        )
        return graph

    @staticmethod
    def create_multi_agent_debate_graph(
        # Surveyor
        surveyor_main_llm: BaseChatModel,
        surveyor_main_llm_system_message: SystemMessage,
        # Proponent
        proponent_main_llm: BaseChatModel,
        proponent_main_llm_system_message: SystemMessage,
        proponent_formatter_llm: BaseChatModel,
        proponent_formatter_llm_system_message: SystemMessage,
        proponent_structured_output_format: type[BaseModel],
        # Opponent
        opponent_main_llm: BaseChatModel,
        opponent_main_llm_system_message: SystemMessage,
        opponent_formatter_llm: BaseChatModel,
        opponent_formatter_llm_system_message: SystemMessage,
        opponent_structured_output_format: type[BaseModel],
        # Adjudicator
        adjudicator_main_llm: BaseChatModel,
        adjudicator_main_llm_system_message: SystemMessage,
        adjudicator_formatter_llm: BaseChatModel,
        adjudicator_formatter_llm_system_message: SystemMessage,
        adjudicator_structured_output_format: type[BaseModel],
        # RAG
        rag,
    ) -> CompiledStateGraph:
        graph_builder = MultiAgentDebateGraphBuilder(state=MultiAgentDebateState)
        # Surveyor
        surveyor = AgentFactory.create_surveyor(
            main_llm=surveyor_main_llm,
            main_llm_system_message=surveyor_main_llm_system_message,
        )
        assert isinstance(surveyor, Surveyor)
        # Adjudicator
        adjudicator = AgentFactory.create_adjudicator(
            main_llm=adjudicator_main_llm,
            main_llm_system_message=adjudicator_main_llm_system_message,
            formatter_llm=adjudicator_formatter_llm,
            schema_pydantic_base_model=adjudicator_structured_output_format,
            formatter_llm_system_message=adjudicator_formatter_llm_system_message,
        )
        assert isinstance(adjudicator, Adjudicator)
        # Proponent
        proponent = AgentFactory.create_proponent(
            main_llm=proponent_main_llm,
            main_llm_system_message=proponent_main_llm_system_message,
            schema_pydantic_base_model=proponent_structured_output_format,
            formatter_llm=proponent_formatter_llm,
            formatter_llm_system_message=proponent_formatter_llm_system_message,
        )
        assert isinstance(proponent, Proponent)
        # Opponent
        opponent = AgentFactory.create_opponent(
            main_llm=opponent_main_llm,
            main_llm_system_message=opponent_main_llm_system_message,
            schema_pydantic_base_model=opponent_structured_output_format,
            formatter_llm=opponent_formatter_llm,
            formatter_llm_system_message=opponent_formatter_llm_system_message,
        )
        assert isinstance(opponent, Opponent)
        graph = graph_builder.build_graph(
            surveyor=surveyor,
            adjudicator=adjudicator,
            proponent=proponent,
            opponent=opponent,
            rag=rag,
        )
        return graph

    @staticmethod
    def create_final_mas_graph(
        # Surveyor
        surveyor_main_llm: BaseChatModel,
        surveyor_main_llm_system_message: SystemMessage,
        # Investigator
        investigator_main_llm: BaseChatModel,
        investigator_main_llm_system_message: SystemMessage,
        investigator_formatter_llm: BaseChatModel,
        investigator_formatter_llm_system_message: SystemMessage,
        investigator_structured_output_format: type[BaseModel],
        # Adjudicator
        adjudicator_main_llm: BaseChatModel,
        adjudicator_main_llm_system_message: SystemMessage,
        adjudicator_formatter_llm: BaseChatModel,
        adjudicator_formatter_llm_system_message: SystemMessage,
        adjudicator_structured_output_format: type[BaseModel],
        # Analyst
        analyst_main_llm: BaseChatModel,
        analyst_main_llm_system_message: SystemMessage,
        analyst_formatter_llm: BaseChatModel,
        analyst_formatter_llm_system_message: SystemMessage,
        analyst_structured_output_format: type[BaseModel],
        # RAG
        rag,
    ) -> CompiledStateGraph:
        graph_builder = FinalMASGraphBuilder(state=FinalMASState)
        # Surveyor
        surveyor = AgentFactory.create_surveyor(
            main_llm=surveyor_main_llm,
            main_llm_system_message=surveyor_main_llm_system_message,
        )
        assert isinstance(surveyor, Surveyor)
        # Investigator
        investigator = AgentFactory.create_investigator(
            main_llm=investigator_main_llm,
            main_llm_system_message=investigator_main_llm_system_message,
            formatter_llm=investigator_formatter_llm,
            schema_pydantic_base_model=investigator_structured_output_format,
            formatter_llm_system_message=investigator_formatter_llm_system_message,
        )
        assert isinstance(investigator, Investigator)
        # Adjudicator
        adjudicator = AgentFactory.create_adjudicator(
            main_llm=adjudicator_main_llm,
            main_llm_system_message=adjudicator_main_llm_system_message,
            formatter_llm=adjudicator_formatter_llm,
            schema_pydantic_base_model=adjudicator_structured_output_format,
            formatter_llm_system_message=adjudicator_formatter_llm_system_message,
        )
        assert isinstance(adjudicator, Adjudicator)
        # Analyst
        analyst = AgentFactory.create_analyst(
            main_llm=analyst_main_llm,
            main_llm_system_message=analyst_main_llm_system_message,
            formatter_llm=analyst_formatter_llm,
            schema_pydantic_base_model=analyst_structured_output_format,
            formatter_llm_system_message=analyst_formatter_llm_system_message,
        )
        assert isinstance(analyst, Analyst)
        graph = graph_builder.build_graph(
            surveyor=surveyor,
            investigator=investigator,
            adjudicator=adjudicator,
            analyst=analyst,
            rag=rag,
        )
        return graph

