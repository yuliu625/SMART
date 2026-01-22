"""
进行详细分析的Agent。

Analysis-Module的分析控制。
基于context-engineering，切换各种专家agent。
"""

from __future__ import annotations

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
from mas.utils.content_annotator import ContentAnnotator
from mas.utils.document_merger import DocumentMerger

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING, Literal, cast
if TYPE_CHECKING:
    from mas.schemas.final_mas_state import FinalMASState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, SystemMessage
    from langchain_core.documents import Document
    from pydantic import BaseModel


class Analyst(BaseAgent):
    """
    执行具体分析的analyst。
    """
    def __init__(
        self,
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
        # formatter相关，对于这个agent可以以不是必需的方法来实现。
        formatter_llm: BaseChatModel,
        schema_pydantic_base_model: type[BaseModel],
        formatter_llm_system_message: SystemMessage,
    ):
        # 需要显式做出最终决策的agent。
        super().__init__(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            main_llm_max_retries=3,
            # 需要结构化输出。
            is_need_structured_output=True,
            formatter_llm=formatter_llm,
            schema_pydantic_base_model=schema_pydantic_base_model,
            formatter_llm_system_message=formatter_llm_system_message,
            formatter_llm_max_retries=3,
        )
        self.main_llm_system_message = main_llm_system_message

    async def process_state(
        self,
        state: FinalMASState,
        config: RunnableConfig,
    ) -> dict:
        # Agent内: 根据last_agent_name，条件处理上一次的消息。
        # assert state.last_agent_name in ('investigator', 'rag')
        last_round_message = self.before_call_analyst(
            remain_retrieve_rounds=state.remaining_retrieve_rounds,
            last_agent_name=cast(Literal['investigator', 'rag'], state.last_agent_name),
            # last_agent_name=state.last_agent_name,
            current_agent_message=state.current_agent_message,
            documents=state.documents,
        )
        # Agent内: 执行分析。
        analyst_result = await self.read_documents(
            analysis_messages=state.analysis_process + [last_round_message],
        )
        # 整个MAS: 构建analysis_process。
        analysis_process = self.after_call_analyst(
            analyst_message=analyst_result.ai_message,
            analysis_process=state.analysis_process,
        )
        # 根据剩余验证轮数调用下一个agent。
        if state.remaining_retrieve_rounds == 0:
            # 已经用完验证次数，需要进行最终决定。
            # 这个判断是system层级冗余稳定判断。
            return dict(
                analysis_process=analysis_process,
                current_message=analyst_result.structured_output.agent_message,
                # HARDCODED: max_retrieve_rounds = 5
                remain_retrieve_rounds=5,  # 重置最大查询次数。
                current_agent_name='investigator',
                last_agent_name='analyst',
            )
        else:
            # 正常运行。
            # Case1: 请求的是investigator，初始化分析。
            ## current_agent_name='analyst', current_documents=[]
            ## last_agent_name='investigator'
            if analyst_result.structured_output.agent_name == 'investigator':
                return dict(
                    analysis_process=analysis_process,
                    current_message=analyst_result.structured_output.agent_message,
                    # HARDCODED: max_retrieve_rounds = 5
                    remain_retrieve_rounds=5,  # 重置最大查询次数。
                    current_agent_name='investigator',
                    last_agent_name='analyst',
                )
            # Case2: 请求rag，读取并分析新的文档内容。
            ## current_agent_name='analyst', current_documents可能为空。
            ## last_agent_name='rag'
            else:
                return dict(
                    analysis_process=analysis_process,
                    current_message=analyst_result.structured_output.agent_message,
                    remain_retrieve_rounds=state.remaining_retrieve_rounds - 1,  # 更新可查询次数。
                    current_agent_name='rag',
                    last_agent_name='analyst',
                )

    # ====主要方法。====
    async def read_documents(
        self,
        analysis_messages: list[AnyMessage],
    ) -> BaseAgentResponse:
        # 获取llm响应。
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
            ] + analysis_messages,
        )
        return response

    # ==== 工具方法。 ====
    def before_call_analyst(
        self,
        remain_retrieve_rounds: int,
        last_agent_name: Literal['investigator', 'rag'],
        current_agent_message: str,
        documents: list[Document],
    ) -> HumanMessage:
        # Case1: RAG返回给Analyst新的信息。
        ## 这种情况下，current_agent_message的内容是query。
        if last_agent_name == 'rag':
            # 整合新的文档。
            document_content = DocumentMerger.merge_text_documents(
                text_documents=documents,
            )
            document_content = f"Query: \n {current_agent_message}\n Result: \n{document_content}"
            rag_message_content = ContentAnnotator.annotate_with_html_comment(
                tag='rag',
                original_text=document_content,
            )
            if remain_retrieve_rounds == 1:
                # Case1.1: 已经用完查询次数。
                rag_message_content = (
                    rag_message_content
                    + f"\n还剩{remain_retrieve_rounds}次查询次数。"
                    + f"\n已经用完查询次数，现在必须做出分析总结交给Investigator进行进一步调查。"
                )
            else:
                # Case1.2: 没有用完次数。
                rag_message_content = (
                    rag_message_content
                    + f"\n还剩{remain_retrieve_rounds}次查询次数。"
                    + f"\n你还可以提出一些点进行查询，或者做出分析总结交给Investigator进行进一步调查。"
                )
            return HumanMessage(content=rag_message_content)
        # Case2: Investigator向Analyst提出需要分析的内容。
        ## 这种情况下remain_retrieve_rounds比不为1。
        else: # last_agent_name == 'investigator':
            # 初始化analyst的信息，并进行分析。
            ## 使用current_agent_message，不使用documents。
            ## assert len(documents) == 0
            investigator_message_content = ContentAnnotator.annotate_with_html_comment(
                tag='investigator',
                original_text=current_agent_message,
            )
            return HumanMessage(content=investigator_message_content)

    # ==== 工具方法。 ====
    def after_call_analyst(
        self,
        analyst_message: AIMessage,
        analysis_process: list[AnyMessage],
    ) -> list[AnyMessage]:
        assert isinstance(analyst_message, AIMessage)
        # 标注身份。
        analyst_last_message_content = ContentAnnotator.annotate_with_html_comment(
            tag='analyst',
            original_text=analyst_message.content,
        )
        # 构建analysis_process。
        analysis_process = analysis_process + [
            AIMessage(content=analyst_last_message_content)
        ]
        return analysis_process

    # ==== 工具方法。 ====
    def process_result_documents(
        self,
        documents: list[Document],
    ) -> str:
        """
        对documents进行处理。

        这里简单的，将文本以xml格式标注并合并。

        Args:
            documents:

        Returns:
            str:
        """
        document_content = DocumentMerger.merge_text_documents(
            text_documents=documents,
        )
        return document_content

