"""

"""

from mas.schemas.mas_state import MASState
from mas.nodes import (
    RagRetrieverFactory,
)
from mas.nodes import AgentFactory
from mas.nodes import route_verification_request
from mas.edges import (
    condition_more_information,
)
from mas.edges import (
    is_need_verification,
    call_analysis_agents,
)

from langgraph.graph import StateGraph
from langgraph.graph.graph import (
    END,
    START,
)

from langgraph.graph.state import CompiledStateGraph
from langchain_core.vectorstores import VectorStore


class MASGraphBuilder:
    def __init__(
        self,
        vector_store: VectorStore,
        pdf_name: str,
    ):
        # 要进行分析的vector_store和pdf。
        self.vector_store = vector_store
        self.pdf_name = pdf_name
        # 构建状态图。
        self.graph_builder = StateGraph(MASState)
        # 构建query-engine。
        self.rag_retriever_factory = RagRetrieverFactory(vector_store=vector_store, pdf_name=pdf_name)
        # 获取相关的agent。
        self.agent_factory = AgentFactory()

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
        self._add_rag_nodes()
        self._add_analysis_nodes()
        self._add_decision_nodes()
        self._add_mas_nodes()
        # 构建3个系统内部的edges。
        self._add_rag_edges()
        self._add_analysis_edges()
        self._add_decision_edges()
        # 连接3个系统。
        self._add_mas_edges()
        graph = self.graph_builder.compile()
        return graph

    def _add_rag_nodes(self):
        """
        注册RAG模块的节点。
        """
        # 从工厂中获取对应的RAG系统。
        # retriever = self.rag_retriever_factory.get_multi_query_retriever()
        # self.graph_builder.add_node('retriever', retriever.run)
        control_retriever = self.rag_retriever_factory.get_control_multi_query_retriever()
        financial_retriever = self.rag_retriever_factory.get_financial_multi_query_retriever()
        strategic_retriever = self.rag_retriever_factory.get_strategic_multi_query_retriever()
        self.graph_builder.add_node('control_retriever', control_retriever.run)
        self.graph_builder.add_node('financial_retriever', financial_retriever.run)
        self.graph_builder.add_node('strategic_retriever', strategic_retriever.run)

    def _add_analysis_nodes(self):
        """
        注册分析模块的agent。
        """
        # analysis相关的agent
        control_document_reader = self.agent_factory.get_control_document_reader()
        control_analyst = self.agent_factory.get_control_analyst()
        financial_document_reader = self.agent_factory.get_financial_document_reader()
        financial_analyst = self.agent_factory.get_financial_analyst()
        strategic_document_reader = self.agent_factory.get_strategic_document_reader()
        strategic_analyst = self.agent_factory.get_strategic_analyst()
        self.graph_builder.add_node('control_document_reader', control_document_reader.run)
        self.graph_builder.add_node('control_analyst', control_analyst.run)
        self.graph_builder.add_node('financial_document_reader', financial_document_reader.run)
        self.graph_builder.add_node('financial_analyst', financial_analyst.run)
        self.graph_builder.add_node('strategic_document_reader', strategic_document_reader.run)
        self.graph_builder.add_node('strategic_analyst', strategic_analyst.run)

    def _add_decision_nodes(self):
        """
        注册决策模块的agent。
        """
        # decision相关的agent
        recognizer = self.agent_factory.get_recognizer()
        validator = self.agent_factory.get_validator()
        arbiter = self.agent_factory.get_arbiter()
        self.graph_builder.add_node('recognizer', recognizer.run)
        self.graph_builder.add_node('validator', validator.run)
        self.graph_builder.add_node('arbiter', arbiter.run)

    def _add_mas_nodes(self):
        """
        注册整个MAS剩余的agent。

        这里是路由相关的agent。
        """
        self.graph_builder.add_node('verification_requests_router', route_verification_request)

    def _add_analysis_edges(self):
        """
        连接分析内部模块。

        这里仅确定document_reader阅读完文档之后，会将结果给analyst分析。
        """
        self.graph_builder.add_edge('control_document_reader', 'control_analyst')
        self.graph_builder.add_edge('financial_document_reader', 'financial_analyst')
        self.graph_builder.add_edge('strategic_document_reader', 'strategic_analyst')

    def _add_decision_edges(self):
        """
        连接决策内部模块。

        这里仅确定recognizer识别之后，validator会根据已有的信息进行分析和验证。
        """
        self.graph_builder.add_edge('recognizer', 'validator')
        # 在不进行验证的情况下，是下面这个。识别之后直接做出仲裁。
        # self.graph_builder.add_edge('recognizer', 'arbiter')

    def _add_rag_edges(self):
        """
        连接RAG模块。
        """
        # 这里后来的实现是将所有的RAG系统都封装在retriever类当中。
        self.graph_builder.add_edge('control_retriever', 'control_document_reader')
        self.graph_builder.add_edge('financial_retriever', 'financial_document_reader')
        self.graph_builder.add_edge('strategic_retriever', 'strategic_document_reader')

    def _add_mas_edges(self):
        """
        连接剩余的节点。

        主要为了连接分析和决策2个子系统。
        """
        # 系统开始于从retrieve产生初始的查询。
        self.graph_builder.add_edge(START, 'recognizer')
        # 获得retriever的结果后，document_reader需要对于文档进行阅读。
        # self.graph_builder.add_edge('retriever', 'control_document_reader')
        # 分析模块，analyst会决定是否进行进一步分析。
        self.graph_builder.add_conditional_edges(
            'control_analyst',
            condition_more_information,
            {
                'True': 'control_retriever',
                'False': 'validator',
            }
        )
        self.graph_builder.add_conditional_edges(
            'financial_analyst',
            condition_more_information,
            {
                'True': 'financial_retriever',
                'False': 'validator',
            }
        )
        self.graph_builder.add_conditional_edges(
            'strategic_analyst',
            condition_more_information,
            {
                'True': 'strategic_retriever',
                'False': 'validator',
            }
        )
        # # validator决定是否需要验证一些信息，如果需要，就修改请求，将相关请求交给路由要求相关分析系统重新进行分析。
        self.graph_builder.add_conditional_edges(
            'validator',
            is_need_verification,
            {
                'True': 'verification_requests_router',
                'False': 'arbiter',
            }
        )
        self.graph_builder.add_conditional_edges(
            'verification_requests_router',
            call_analysis_agents,
            ['arbiter', 'control_analyst', 'financial_analyst', 'strategic_analyst']
        )
        # # arbiter进行最终仲裁，完成全部分析。
        self.graph_builder.add_edge('arbiter', END)

