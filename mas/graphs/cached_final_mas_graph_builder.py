"""
Design Patter: MAS

构建整个MAS的方法。
"""

from __future__ import annotations
from loguru import logger

# State
from mas.schemas.final_mas_state import FinalMASState # 由于构建graph_builder需要使用到MASState，因此不能仅以类型声明。
# Nodes
from mas.agent_nodes.analysis_agents.analyst import Analyst
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.investigator import Investigator
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
# Edges
from mas.edges.analysis_condition_edges import (
    is_need_more_information,
)
from mas.edges.decision_condition_edges import (
    is_need_validation,
)

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


class CachedFinalMASGraphBuilder:
    """
    计算图的构造器。
    """
    def __init__(
        self,
        state: type[FinalMASState],
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
        rag,
        checkpointer: BaseCheckpointSaver | None = None,
    ) -> CompiledStateGraph:
        self._add_nodes(
            surveyor=surveyor,
            investigator=investigator,
            adjudicator=adjudicator,
            analyst=analyst,
            rag=rag,
        )
        self._add_edges()
        graph = self.graph_builder.compile(checkpointer=checkpointer)
        logger.info(f"Built cached final MAS graph.")
        return graph

    def _add_nodes(
        self,
        surveyor: Surveyor,
        investigator: Investigator,
        adjudicator: Adjudicator,
        analyst: Analyst,
        rag,
    ):
        """
        注册MAS的nodes。
        """
        # Decision Module
        self.graph_builder.add_node('surveyor', surveyor.process_state)
        self.graph_builder.add_node('investigator', investigator.process_state)
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
        # self.graph_builder.add_edge(START, 'surveyor')
        # surveyor的初步结论交给investigator进行分析。
        # self.graph_builder.add_edge('surveyor', 'investigator')

        # CHANGE: 系统的开始由 investigator 开始，surveyor 的结果从缓存中加载。
        self.graph_builder.add_edge(START, 'investigator')

        # investigator根据情况选择给adjudicator提交总结或要求analyst进行分析。
        self.graph_builder.add_conditional_edges(
            'investigator',
            is_need_validation,
            {
                'analyst': 'analyst',
                'adjudicator': 'adjudicator',
            },
        )
        # analyst根据情况选择是否检索信息。
        self.graph_builder.add_conditional_edges(
            'analyst',
            is_need_more_information,
            {
                'rag': 'rag',
                'investigator': 'investigator',
            },
        )
        # RAG返回的结果一定交给analyst进行处理。
        self.graph_builder.add_edge('rag', 'analyst')
        # Adjudicator读取全部的信息，并做出最终的判断。
        self.graph_builder.add_edge('adjudicator', END)

