"""
简单的MAS design pattern，基于固定序列流。
"""

from __future__ import annotations

from mas.schemas.mas_state import MASState # 由于构建graph_builder需要使用到MASState，因此不能仅以类型声明。
from mas.agent_nodes.agent_factory import AgentFactory

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
        state: type[MASState],
    ):
        # 初始化计算图构建。实际中不会以变量传入state，因为state为数据类，更多实现方法为以包导入并写死。
        self.graph_builder = StateGraph(state)
        # 注册需要的工具。

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
        # Decision Module
        surveyor = AgentFactory.create_surveyor()
        investigator = AgentFactory.create_investigator()
        adjudicator = AgentFactory.create_adjudicator()
        self.graph_builder.add_node('surveyor', surveyor.process_state)
        self.graph_builder.add_node('investigator', investigator.process_state)
        self.graph_builder.add_node('adjudicator', adjudicator.process_state)

    def _add_edges(self):
        """
        注册MAS的edges。
        """
        self.graph_builder.add_edge(START, 'surveyor')
        self.graph_builder.add_edge('surveyor', 'investigator')
        self.graph_builder.add_edge('adjudicator', END)

