"""
design pattern: 基于固定序列流。

接近于最终MAS中的仅decision module。
"""

from __future__ import annotations
from loguru import logger

from mas.schemas.single_agent_mas_state import SingleAgentMASState
from mas.agent_nodes.analysis_agents.analyst import Analyst
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.investigator import Investigator
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
# from mas.agent_nodes.agent_factory import AgentFactory

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph
    from langgraph.checkpoint.base import BaseCheckpointSaver


class SequentialMASGraphBuilder:
    """
    计算图的构造器。
    """
    def __init__(
        self,
        state: type[SingleAgentMASState],
    ):
        # 初始化计算图构建。实际中不会以变量传入state，因为state为数据类，更多实现方法为以包导入并写死。
        self.graph_builder = StateGraph(state)
        # 注册需要的工具。

    def build_graph(
        self,
        surveyor: Surveyor,
        investigator: Investigator,
        adjudicator: Adjudicator,
        analyst: Analyst,
        checkpointer: BaseCheckpointSaver | None = None,
    ) -> CompiledStateGraph:
        self._add_nodes(
            surveyor=surveyor,
            investigator=investigator,
            adjudicator=adjudicator,
            analyst=analyst,
        )
        self._add_edges()
        graph = self.graph_builder.compile(checkpointer=checkpointer)
        logger.info(f"Built sequential mas graph.")
        return graph

    def _add_nodes(
        self,
        surveyor: Surveyor,
        investigator: Investigator,
        adjudicator: Adjudicator,
        analyst: Analyst,
    ):
        """
        注册MAS的nodes。
        """
        # Decision Module
        # surveyor = AgentFactory.create_surveyor()
        # investigator = AgentFactory.create_investigator()
        # adjudicator = AgentFactory.create_adjudicator()
        self.graph_builder.add_node('surveyor', surveyor.process_state)
        self.graph_builder.add_node('investigator', investigator.process_state)
        self.graph_builder.add_node('adjudicator', adjudicator.process_state)
        self.graph_builder.add_node('analyst', analyst.process_state)

    def _add_edges(self):
        """
        注册MAS的edges。
        """
        # 输入的内容由surveyor进行处理。
        self.graph_builder.add_edge(START, 'surveyor')
        # Investigator根据整体的内容进行分析。
        self.graph_builder.add_edge('surveyor', 'investigator')
        # self.graph_builder.add_edge('investigator', 'analyst')
        # self.graph_builder.add_edge('analyst', 'rag')
        # self.graph_builder.add_edge('rag', 'analyst')
        # self.graph_builder.add_edge('analyst', 'investigator')
        # Adjudicator读取全部的信息，并做出最终的判断。
        self.graph_builder.add_edge('adjudicator', END)

