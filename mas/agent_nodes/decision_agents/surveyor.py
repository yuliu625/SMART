"""
识别者。

Decision-Module，起始阶段agent。
"""

from __future__ import annotations
from loguru import logger

from mas.agent_nodes.base_agent import BaseAgent, BaseAgentResponse
from mas.utils.content_annotator import ContentAnnotator

from langchain_core.messages import HumanMessage, AIMessage

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.schemas.final_mas_state import FinalMASState
    from langchain_core.runnables import RunnableConfig
    from langchain_core.language_models import BaseChatModel
    from langchain_core.messages import AnyMessage, AIMessage, SystemMessage


class Surveyor(BaseAgent):
    """
    整体公司风险识别者。

    长文档阅读能力。

    进行:
        - 读取原始文本内容，识别公司架构。
        - 初步识别风险，分派验证任务。

    架构:
        - 在MAS中的decision模块。
        - 在整个MAS开始，仅运行一次。
    """
    def __init__(
        self,
        main_llm: BaseChatModel,
        main_llm_system_message: SystemMessage,
    ):
        # 基本的agent，不对于输出进行限制。
        super().__init__(
            main_llm=main_llm,
            main_llm_system_message=main_llm_system_message,
            main_llm_max_retries=3,
            # 不需要结构化输出。
            is_need_structured_output=False,
            formatter_llm=None,
            schema_pydantic_base_model=None,
            formatter_llm_system_message=None,
            formatter_llm_max_retries=3,
        )
        self.main_llm_system_message = main_llm_system_message

    async def process_state(
        self,
        state: FinalMASState,
        config: RunnableConfig,
    ) -> dict:
        """
        由于surveyor为初始化运行且仅运行一次，surveyor不专门设置chat-history，由surveyor完成全部的初始化。

        Args:
            state (FinalMASState): 使用的state。需要字段:
                - original_pdf_text: 原始文档的文本信息。
            config (RunnableConfig): 运行设置。

        Returns:
            dict: 进行更新的字段，包括:
                - decision_shared_messages: 初始化的decision_shared_messages。
                - current_agent_name: 下一个运行的agent。冗余字段，固定边一定指向 'investigator'。
        """
        recognizer_response = await self.read_original_pdf_text(
            original_pdf_text=state.original_pdf_text,
        )
        # 获得共享的memory。
        decision_shared_messages = self.initiate_decision_shared_messages(
            surveyor_message=recognizer_response.ai_message,  # 这里的response只需要surveyor的ai_message。
        )
        assert isinstance(decision_shared_messages, list)
        assert len(decision_shared_messages) == 1
        assert isinstance(decision_shared_messages[0], HumanMessage)  # 这里需要是HumanMessage才可以启动后续的Investigator。
        return dict(
            decision_shared_messages=decision_shared_messages,
            current_agent_name='investigator',  # 并没有发出请求，但是下一个一定是validator。
            last_agent_name='surveyor',
        )

    # ====主要方法。====
    async def read_original_pdf_text(
        self,
        original_pdf_text: str,
    ) -> BaseAgentResponse:
        """
        读取原始文档的文本，以decision模块的decision_shared_messages返回。

        Args:
            original_pdf_text (str): 原始文档的文本信息。

        Returns:
            AIMessage: 初始化的decision_shared_messages。agent_request为空。
        """
        # 对于初始pdf的文本内容进行分析。
        response = await self.a_call_llm_with_retry(
            messages=[
                self.main_llm_system_message,
                HumanMessage(content=original_pdf_text),
            ],
        )
        return response
        # return AgentProcessedResult(
        #     messages=response.ai_message,
        #     agent_request='validator',  # 并没有发出请求，但是下一个一定是validator。
        # )

    # ====工具方法。====
    def initiate_decision_shared_messages(
        self,
        surveyor_message: AIMessage,
    ) -> list[AnyMessage]:
        """
        将surveyor初始识别的结果转换，封装为初始decision_shared_messages。
        对于shared_messages，主要使用者为investigator，surveyor以HumanMessage初始化作为启动。

        Args:
            surveyor_message (AIMessage): surveyor初始识别的结果。

        Returns:
            list[AnyMessage]: decision_shared_messages。
                这个专用方法实际返回的是decision_shared_messages，为list[HumanMessage]，仅一条初始的human-message。
        """
        assert isinstance(surveyor_message, AIMessage)
        # 标注身份。
        surveyor_first_message_content = ContentAnnotator.annotate_with_html_comment(
            tag='surveyor',
            original_text=surveyor_message.content,
        )
        # 构建decision_shared_messages。
        decision_shared_messages = [
            HumanMessage(content=surveyor_first_message_content),  # 把surveyor的信息放进去。
        ]
        return decision_shared_messages

