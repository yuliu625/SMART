"""
整个MAS的graph的计算状态。
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.documents import Document
    from langchain_core.messages import AnyMessage


class FinalMASState(BaseModel):
    """
    最终构建的MAS的state。
    """
    # MAS条件控制。
    ## current related, 整个MAS控制相关。
    current_agent_name: str = Field(
        default="adjudicator",
        description="当前应该运行的agent的名字。",
    )
    current_message: str = Field(
        default="",
        description="当前agent可能会使用的信息。",
    )

    # Decision Module
    ## 共用字段。
    decision_shared_messages: list[AnyMessage] = Field(
        default_factory=list,
        description="所有decision中的agent共用的messages。",
    )
    ## Adjudicator. 代表最终结果的重要字段。
    final_decision: dict = Field(
        default_factory=dict,
        description="Adjudicator结构化输出的最终决策。",
    )
    ## Surveyor. 启动。
    original_pdf_text: str = Field(
        description="原始的pdf文档的text。专门用一个字段是为了避免和current_message出现问题。",
    )
    ## Investigator
    ### 剩余验证步骤，如果用完，就必须交给adjudicator进行最终决定。
    remaining_validation_rounds: int = Field(
        default=10,
        description="Investigator剩余可进行验证的次数。",
    )
    is_more_information: bool = Field(
        default=False,
        description="Analyst选择是否需要进一步的分析。",
    )
    ## Investigator要求analysis模块要进行重新分析的{agent: content}。
    is_need_verification: bool = Field(
        default=False,
        description="Investigator决定是否需要Analyst进一步分析。",
    )

    # Analysis Module
    ## Analyst
    remaining_retrieve_rounds: int = Field(
        default=5,
        description="analyst剩余可以进行查询次数。",
    )
    analyst_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="Analyst获得的信息和分析过程。",
    )
    # query_result_history: list[Document] = Field(
    #     default_factory=list,
    #     description="历史查询的结果，返回新查询结果是用于去重。",
    # )
    # analysis agents
    # document_reader_chat_history: list[AnyMessage] = Field(
    #     default_factory=list,
    #     description="文档阅读的历史",
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

