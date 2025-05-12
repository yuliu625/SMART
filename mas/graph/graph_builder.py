"""

"""

from .states.mas_state import MASState
from .nodes import AgentFactory
from .nodes.mas_nodes import route_verification_request
from .edges.decision_edges import (
    condition_final_round,
)
from .edges.mas_edges import (
    is_need_verification,
)

from langgraph.graph import StateGraph
from langgraph.graph.graph import (
    END,
    START,
    CompiledGraph,
    Graph,
    Send,
)

from langgraph.graph.state import CompiledStateGraph


class MASGraph:
    def __init__(
        self,
    ):
        # 构建状态图。
        self.graph_builder = StateGraph(MASState)
        # 获取相关的agent。
        self.agent_factory = AgentFactory()
        # decision相关的agent
        self.recognizer = self.agent_factory.get_recognizer()
        self.validator = self.agent_factory.get_validator()
        self.arbiter = self.agent_factory.get_arbiter()

    def build_graph(
        self,
    ) -> CompiledStateGraph:
        """
        构建整个图。

        注册所有节点，然后再连接。

        Returns:
            已经编译好的可运行的状态图。
        """
        # 注册nodes。
        self._add_analysis_nodes()
        self._add_decision_nodes()
        self._add_mas_nodes()
        # 构建2个系统内部的edges。
        self._add_analysis_edges()
        self._add_decision_edges()
        # 连接2个系统。
        self._add_mas_edges()
        graph = self.graph_builder.compile()
        return graph

    def _add_analysis_nodes(self):
        """
        注册分析模块的agent。
        """

    def _add_decision_nodes(self):
        """
        注册决策模块的agent。
        """
        self.graph_builder.add_node('recognizer', self.recognizer.run)
        self.graph_builder.add_node('validator', self.validator.run)
        self.graph_builder.add_node('arbiter', self.arbiter.run)

    def _add_mas_nodes(self):
        """
        注册整个MAS剩余的agent。

        这里是路由相关的agent。
        """
        self.graph_builder.add_node('verification_requests_router', route_verification_request)

    def _add_analysis_edges(self):
        ...

    def _add_decision_edges(self):
        """
        连接决策内部模块。

        这里仅确定recognizer识别之后，validator会根据已有的信息进行分析和验证。
        """
        self.graph_builder.add_edge('recognizer', 'validator')
        # 在不进行验证的情况下，是下面这个。识别之后直接做出仲裁。
        # self.graph_builder.add_edge('recognizer', 'arbiter')

    def _add_mas_edges(self):
        """
        连接剩余的节点。

        主要为了连接分析和决策2个子系统。
        """
        # 最后，创建整个MAS的开始和结束。
        self.graph_builder.add_edge(START, 'recognizer')
        # validator决定是否需要验证一些信息，如果需要，就修改请求，将相关请求交给路由要求相关分析系统重新进行分析。
        self.graph_builder.add_conditional_edges(
            'validator',
            is_need_verification,
            {
                'True': 'verification_requests_router',
                'False': 'arbiter',
            }
        )
        self.graph_builder.add_edge('verification_requests_router', 'recognizer')
        # arbiter进行最终仲裁，完成全部分析。
        self.graph_builder.add_edge('arbiter', END)

