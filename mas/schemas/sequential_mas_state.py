"""
Sequential Workflow State

State definition of sequential mas.
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage
from langchain_core.documents import Document

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class SequentialMASState(BaseModel):
    """
    Sequential MAS中使用的state。

    实际等同:
        - 在有RAG支持下的最小必要字段。
        -   Decision::Surveyor,Adjudicator,
            Analysis::Analyst,
            RAG::Retriever
            需要的字段。
    """
    # MAS条件控制。
    ## current related, 整个MAS控制相关。
    current_agent_name: str = Field(
        default="adjudicator",
        description="当前应该运行的agent的名字。",
    )
    last_agent_name: str = Field(
        default="start",
        description="上一个agent的名字，用于追寻任务和请求的来源。",
    )
    ## 为兼容性保留。
    ## 在这个实现中，仅为传递给RAG的初始查询。
    current_message: str = Field(
        default="",
        description="当前agent可能会使用的信息。",
    )

    # Decision Module
    ## 共用字段。该实现需要额外处理。
    decision_shared_messages: list[AnyMessage] = Field(
        default_factory=list,
        description="所有decision中的agent共用的messages。在这个实现中，是adjudicator专用。使用需要额外处理。",
    )
    ## Adjudicator. 代表最终结果的重要字段。
    final_decision: dict = Field(
        default_factory=dict,
        description="Adjudicator结构化输出的最终决策。",
    )

    # Analysis Module
    ## Analyst
    # analyst_messages: list[AnyMessage] = Field(
    #     default_factory=list,
    #     description="Analyst获得的信息和分析过程。",
    # )
    # remaining_retrieve_rounds: int = Field(
    #     default=5,
    #     description="Analyst剩余可以进行查询次数。",
    # )

    # RAG
    ## 检索结果/当前analyst可以进行分析的材料。
    current_documents: list[Document] = Field(
        default_factory=list,
        description="RAG模块返回的结果。",
    )
    ## RAG运行所需要的query由current_message字段复用。
    # query: str = Field(
    #     default="",
    #     description="RAG模块需要执行的查询。"
    # )

