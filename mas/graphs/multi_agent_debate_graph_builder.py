"""
Design Pattern: multi-agent debate

fixed rounds and independent judge
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
    check_next_agent,
    is_debate_end,
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
    multi-agent debate graph
    """
    def __init__(
        self,
        state: type[MultiAgentDebateState],
    ):
        # 初始化计算图构建。实际中不会以变量传入state，因为state为数据类，更多实现方法为以包导入并写死。
        self.graph_builder = StateGraph(state)

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
        ## 符合函数式编程的 node ，注册 2 次无副作用。
        self.graph_builder.add_node('proponent_rag', rag.process_state)
        self.graph_builder.add_node('opponent_rag', rag.process_state)

    def _add_edges(self):
        """
        注册 MAS 的 edges 。
        """
        # 输入的内容由 surveyor 进行处理。
        self.graph_builder.add_edge(START, 'surveyor')
        # Proponent 和 opponent 交替进行分析和判断。
        ## 首先约定由 proponent_rag 开始。
        self.graph_builder.add_edge('surveyor', 'proponent_rag')
        ## 实验用 proponent
        # 根据情况选择选择 rag opponent adjudicator 。
        self.graph_builder.add_edge('proponent_rag', 'proponent')
        ## 实验用 opponent
        self.graph_builder.add_edge('proponent', 'opponent_rag')
        self.graph_builder.add_edge('opponent_rag', 'opponent')
        ## 判断 debate 是否终止。
        self.graph_builder.add_conditional_edges(
            'opponent',
            is_debate_end,
            {
                'proponent': 'proponent_rag',
                'adjudicator': 'adjudicator',
            },
        )
        # Adjudicator 读取全部的信息，并做出最终的判断。
        self.graph_builder.add_edge('adjudicator', END)

