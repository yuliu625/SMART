"""
分析系统子图的构建。
"""

from __future__ import annotations

from mas.nodes.agent_factory import AgentFactory
from mas.edges.analysis_edges import is_need_more_information

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph
    from langgraph.checkpoint.base import BaseCheckpointSaver


class AnalysisGraphBuilder:
    def __init__(self, state):
        self.graph_builder = StateGraph(state)

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
        self.graph_builder.add_edge(START, 'analyst')
        self.graph_builder.add_conditional_edges(
            'analyst',
            is_need_more_information,
            {
                True: 'document_reader',
                False: END,
            }
        )
        self.graph_builder.add_edge('document_reader', 'analyst')

