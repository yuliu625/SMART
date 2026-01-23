"""
Benchmark.
"""

from __future__ import annotations
from loguru import logger

# State
from mas.schemas.single_agent_mas_state import SingleAgentMASState
# Nodes
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
# from mas.agent_nodes.agent_factory import AgentFactory

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.agent_nodes.base_agent import BaseAgent
    from langgraph.graph.state import CompiledStateGraph
    from langgraph.checkpoint.base import BaseCheckpointSaver


class SingleAgentMASGraphBuilder:
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
        adjudicator: Adjudicator,
        checkpointer: BaseCheckpointSaver | None = None,
    ) -> CompiledStateGraph:
        self._add_nodes(
            adjudicator=adjudicator,
        )
        self._add_edges()
        graph = self.graph_builder.compile(checkpointer=checkpointer)
        logger.info(f"Built single agent MAS graph.")
        return graph

    def _add_nodes(
        self,
        adjudicator: Adjudicator,
    ):
        """
        注册MAS的nodes。
        """
        # Decision Module
        # adjudicator = AgentFactory.create_adjudicator()
        self.graph_builder.add_node('adjudicator', adjudicator.process_state)

    def _add_edges(self):
        """
        注册MAS的edges。
        """
        # 输入内容后，直接输入给adjudicator。
        self.graph_builder.add_edge(START, 'adjudicator')
        # Adjudicator完成解析，整个流程结束。
        self.graph_builder.add_edge('adjudicator', END)

