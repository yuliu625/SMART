"""
Design Pattern: multi-agent debate
"""

from __future__ import annotations
from loguru import logger

# State
from mas.schemas.multi_agent_debate_state import MultiAgentDebateState
# Nodes
from mas.agent_nodes.analysis_agents.proponent import Proponent
from mas.agent_nodes.analysis_agents.opponent import Opponent
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
# Edges
from mas.edges.multi_agent_condition_edges import (
    is_need_transfer_to_opponent,
    is_need_transfer_to_proponent,
)

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph
    from langgraph.checkpoint.base import BaseCheckpointSaver


class MultiAgentDebateGraphBuilder:
    """
    计算图的构造器。
    """
    def __init__(
        self,
        state: type[MultiAgentDebateState],
    ):
        # 初始化计算图构建。实际中不会以变量传入state，因为state为数据类，更多实现方法为以包导入并写死。
        self.graph_builder = StateGraph(state)
        # 注册需要的工具。
        raise NotImplementedError("权衡是否需要引入 RAG ?")

    def build_graph(
        self,
        surveyor: Surveyor,
        adjudicator: Adjudicator,
        proponent: Proponent,
        opponent: Opponent,
        rag,
        checkpointer: BaseCheckpointSaver | None = None,
    ) -> CompiledStateGraph:
        self._add_nodes(
            surveyor=surveyor,
            adjudicator=adjudicator,
            proponent=proponent,
            opponent=opponent,
            rag=rag,
        )
        self._add_edges()
        graph = self.graph_builder.compile(checkpointer=checkpointer)
        return graph

    def _add_nodes(
        self,
        surveyor: Surveyor,
        adjudicator: Adjudicator,
        proponent: Proponent,
        opponent: Opponent,
        rag,
    ):
        """
        注册 MAS 的 nodes 。
        """
        # Decision Module
        self.graph_builder.add_node('surveyor', surveyor.process_state)
        self.graph_builder.add_node('adjudicator', adjudicator.process_state)
        # Analysis Module
        self.graph_builder.add_node('proponent', proponent.process_state)
        self.graph_builder.add_node('opponent', opponent.process_state)
        # RAG
        self.graph_builder.add_node('rag', rag.process_state)

    def _add_edges(self):
        """
        注册 MAS 的 edges 。
        """
        # 输入的内容由 surveyor 进行处理。
        self.graph_builder.add_edge(START, 'surveyor')
        # Proponent 和 opponent 交替进行分析和判断。
        ## 首先约定由 proponent 开始。
        self.graph_builder.add_edge('surveyor', 'proponent')
        ## proponent 根据情况选择选择 rag opponent adjudicator 。
        self.graph_builder.add_conditional_edges(
            'proponent',
            is_need_transfer_to_opponent,
            {
                'opponent': 'rag',  # HACK: 转移控制权给对方前，进行检索。
                'adjudicator': 'adjudicator',
            },
        )
        ## opponent 根据情况选择选择 rag proponent adjudicator 。
        self.graph_builder.add_conditional_edges(
            'opponent',
            is_need_transfer_to_proponent,
            {
                'proponent': 'rag',  # HACK: 转移控制权给对方前，进行检索。
                'adjudicator': 'adjudicator',
            },
        )
        # RAG 返回的结果一定交给 proponent 或 opponent 进行处理。
        self.graph_builder.add_edge('rag', 'proponent')
        self.graph_builder.add_edge('rag', 'opponent')
        # Adjudicator 读取全部的信息，并做出最终的判断。
        self.graph_builder.add_edge('adjudicator', END)

