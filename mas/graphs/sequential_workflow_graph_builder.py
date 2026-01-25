"""
Design Pattern: Sequential Workflow。

接近于最终MAS中的仅decision module。
"""

from __future__ import annotations
from loguru import logger

# State
from mas.schemas.sequential_workflow_state import SequentialWorkflowState
# Nodes
from mas.agent_nodes.analysis_agents.analyst import Analyst
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator

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


class SequentialWorkflowGraphBuilder:
    """
    计算图的构造器。
    """
    def __init__(
        self,
        state: type[SequentialWorkflowState],
    ):
        # 初始化计算图构建。实际中不会以变量传入state，因为state为数据类，更多实现方法为以包导入并写死。
        self.graph_builder = StateGraph(state)
        # 注册需要的工具。

    def build_graph(
        self,
        surveyor: Surveyor,
        adjudicator: Adjudicator,
        analyst: Analyst,
        rag,
        checkpointer: BaseCheckpointSaver | None = None,
    ) -> CompiledStateGraph:
        self._add_nodes(
            surveyor=surveyor,
            adjudicator=adjudicator,
            analyst=analyst,
            rag=rag,
        )
        self._add_edges()
        graph = self.graph_builder.compile(checkpointer=checkpointer)
        logger.info(f"Built sequential MAS graph.")
        return graph

    def _add_nodes(
        self,
        surveyor: Surveyor,
        adjudicator: Adjudicator,
        analyst: Analyst,
        rag,
    ):
        """
        注册MAS的nodes。
        """
        # Decision Module
        self.graph_builder.add_node('surveyor', surveyor.process_state)
        self.graph_builder.add_node('adjudicator', adjudicator.process_state)
        # Analysis Module
        self.graph_builder.add_node('analyst', analyst.process_state)
        # RAG
        self.graph_builder.add_node('rag', rag.process_state)

    def _add_edges(self):
        """
        注册MAS的edges。
        """
        # 输入的内容由surveyor进行处理。
        self.graph_builder.add_edge(START, 'surveyor')
        # Surveyor分析完后，直接进行查询。
        self.graph_builder.add_edge('surveyor', 'rag')
        # 查询后的结果，直接进行组合，不进行额外处理。
        self.graph_builder.add_edge('rag', 'analyst')
        # 结果直接交给adjudicator。
        self.graph_builder.add_edge('analyst', 'adjudicator')
        # Adjudicator读取全部的信息，并做出最终的判断。
        self.graph_builder.add_edge('adjudicator', END)

