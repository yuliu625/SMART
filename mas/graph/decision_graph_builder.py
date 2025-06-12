"""
决策系统子图的构建。
"""

from __future__ import annotations

from mas.schemas.decision_state import DecisionState
from mas.nodes.agent_factory import AgentFactory

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph
    from langgraph.checkpoint.base import BaseCheckpointSaver


class DecisionGraphBuilder:
    def __init__(self):
        self.graph_builder = StateGraph(DecisionState)

    def build_graph(
        self,
        checkpointer: BaseCheckpointSaver | None = None,
    ) -> CompiledStateGraph:
        self._add_nodes()
        self._add_edges()
        graph = self.graph_builder.compile(checkpointer=checkpointer)
        return graph

    def _add_nodes(self):
        """
        注册MAS的nodes。
        """

    def _add_edges(self):
        """
        注册MAS的edges。
        """

