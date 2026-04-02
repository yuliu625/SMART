"""
整个 MAS 的 graph 的计算状态。
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.documents import Document
from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class FinalMASState(BaseModel):
    """
    最终构建的 MAS 的 state 。
    """
    # MAS条件控制。
    ## current related, 整个MAS控制相关。
    current_agent_name: str = Field(
        default="surveyor",
        description="当前应该运行的 agent 的名字。",
    )
    last_agent_name: str = Field(
        default="start",
        description="上一个 agent 的名字，用于追寻任务和请求的来源。",
    )
    current_message: str = Field(
        default="",
        description="当前 agent 可能会使用的信息。",
    )

    # Decision Module
    ## 共用字段。
    decision_shared_messages: list[AnyMessage] = Field(
        default_factory=list,
        description="所有 decision 中的 agent 共用的 messages 。",
    )
    ## Adjudicator. 代表最终结果的重要字段。
    final_decision: dict = Field(
        default_factory=dict,
        description="Adjudicator 结构化输出的最终决策。",
    )
    ## Surveyor. 启动。
    original_pdf_text: str = Field(
        description="原始的 pdf 文档的 text 。专门用一个字段是为了避免和 current_message 出现问题。",
    )
    ## Investigator
    ### 剩余验证步骤，如果用完，就必须交给adjudicator进行最终决定。
    remaining_validation_rounds: int = Field(
        default=10,
        description="Investigator 剩余可进行验证的次数。",
    )

    # Analysis Module
    analysis_process_history: list[list[AnyMessage]] = Field(
        default_factory=list,
        description="全局 Analysis 的记录。仅在结束分析时留档而触发。",
    )
    ## Analyst
    analysis_process: list[AnyMessage] = Field(
        default_factory=list,
        description="Analyst 获得的信息和分析过程。",
    )
    remaining_retrieve_rounds: int = Field(
        default=5,
        description="Analyst 剩余可以进行查询次数。",
    )
    ## Document Reader
    # document_reader_chat_history: list[AnyMessage] = Field(
    #     default_factory=list,
    #     description="文档阅读的历史",
    # )

    # RAG
    ## 检索结果/当前analyst可以进行分析的材料。
    current_documents: list[Document] = Field(
        default_factory=list,
        description="RAG 模块返回的结果。",
    )
    ## RAG运行所需要的query由current_message字段复用。
    # query: str = Field(
    #     default="",
    #     description="RAG模块需要执行的查询。"
    # )
    # query_result_history: list[Document] = Field(
    #     default_factory=list,
    #     description="历史查询的结果，返回新查询结果是用于去重。",
    # )

