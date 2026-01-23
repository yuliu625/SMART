"""
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
    from langgraph.graph.state import CompiledStateGraph
    from langgraph.checkpoint.base import BaseCheckpointSaver


class FinalMASGraphBuilder:
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
        logger.info(f"Built final MAS graph.")
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
        self.graph_builder.add_edge(START, 'surveyor')
        # surveyor的初步结论交给investigator进行分析。
        self.graph_builder.add_edge('surveyor', 'investigator')
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


#     def _add_analysis_edges(self):
#         """
#         连接分析内部模块。
#
#         这里仅确定document_reader阅读完文档之后，会将结果给analyst分析。
#         """
#         self.graph_builder.add_edge('control_document_reader', 'control_analyst')
#         self.graph_builder.add_edge('financial_document_reader', 'financial_analyst')
#         self.graph_builder.add_edge('strategic_document_reader', 'strategic_analyst')
#
#     def _add_decision_edges(self):
#         """
#         连接决策内部模块。
#
#         这里仅确定recognizer识别之后，validator会根据已有的信息进行分析和验证。
#         """
#         self.graph_builder.add_edge('recognizer', 'validator')
#         # 在不进行验证的情况下，是下面这个。识别之后直接做出仲裁。
#         # self.graph_builder.add_edge('recognizer', 'arbiter')
#
#     def _add_rag_edges(self):
#         """
#         连接RAG模块。
#         """
#         # 这里后来的实现是将所有的RAG系统都封装在retriever类当中。
#         self.graph_builder.add_edge('control_retriever', 'control_document_reader')
#         self.graph_builder.add_edge('financial_retriever', 'financial_document_reader')
#         self.graph_builder.add_edge('strategic_retriever', 'strategic_document_reader')
#
#     def _add_mas_edges(self):
#         """
#         连接剩余的节点。
#
#         主要为了连接分析和决策2个子系统。
#         """
#         # 系统开始于从retrieve产生初始的查询。
#         self.graph_builder.add_edge(START, 'recognizer')
#         # 获得retriever的结果后，document_reader需要对于文档进行阅读。
#         # self.graph_builder.add_edge('retriever', 'control_document_reader')
#         # 分析模块，analyst会决定是否进行进一步分析。
#         self.graph_builder.add_conditional_edges(
#             'control_analyst',
#             condition_more_information,
#             {
#                 'True': 'control_retriever',
#                 'False': 'validator',
#             }
#         )
#         self.graph_builder.add_conditional_edges(
#             'financial_analyst',
#             condition_more_information,
#             {
#                 'True': 'financial_retriever',
#                 'False': 'validator',
#             }
#         )
#         self.graph_builder.add_conditional_edges(
#             'strategic_analyst',
#             condition_more_information,
#             {
#                 'True': 'strategic_retriever',
#                 'False': 'validator',
#             }
#         )
#         # # validator决定是否需要验证一些信息，如果需要，就修改请求，将相关请求交给路由要求相关分析系统重新进行分析。
#         self.graph_builder.add_conditional_edges(
#             'validator',
#             is_need_verification,
#             {
#                 'True': 'verification_requests_router',
#                 'False': 'arbiter',
#             }
#         )
#         self.graph_builder.add_conditional_edges(
#             'verification_requests_router',
#             call_analysis_agents,
#             ['arbiter', 'control_analyst', 'financial_analyst', 'strategic_analyst']
#         )
#         # # arbiter进行最终仲裁，完成全部分析。
#         self.graph_builder.add_edge('arbiter', END)

