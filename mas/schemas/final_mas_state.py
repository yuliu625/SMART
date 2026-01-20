"""
整个MAS的graph的计算状态。
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.documents import Document
    from langchain_core.messages import AnyMessage


class MASState(BaseModel):
    # MAS条件控制。
    # current related, 整个MAS控制相关。
    current_agent_name: str = Field(
        default="arbiter",
        description="当前执行操作的agent的名字",
    )
    current_message: str = Field(
        default="",
        description="调用当前agent的上一个agent传递的信息。",
    )

    # Decision Module
    decision_shared_messages: list[AnyMessage] = Field(
        default_factory=list,
        description="所有decision中的agent共用的messages。",
    )
    ## Surveyor
    original_pdf_text: str = Field(
        description="原始的pdf文档的text。专门用一个字段是为了避免和current_message出现问题。",
    )
    ## Investigator
    ### 剩余验证步骤，如果用完，就必须交给adjudicator进行最终决定。
    remaining_validation_rounds: int = Field(
        default=10,
        description="Investigator剩余可进行验证的次数。",
    )
    more_information: bool = Field(
        default=False,
        description="Analyst选择是否需要进一步的分析。",
    )
    ## validator要求analysis模块要进行重新分析的{agent: content}。
    is_need_verification: bool = Field(
        default=False,
        description="Investigator决定是否需要Analyst进一步分析。",
    )
    ## Adjudicator
    final_decision: dict = Field(
        default_factory=dict,
        description="Adjudicator结构化输出的最终决策。",
    )

    # Analysis Module
    remaining_retrieve_rounds: int = Field(
        default=5,
        description="analyst剩余可以进行查询次数。",
    )
    last_round_result_number: int = Field(
        default=-1,
        description="上轮获取的结果的数量",
    )
    query_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="query重写使用。查询的历史，用于rag中的agent进行对话。",
    )
    query_result_history: list[Document] = Field(
        default_factory=list,
        description="历史查询的结果，返回新查询结果是用于去重。",
    )
    ## query result
    current_query_results: list[Document] = Field(
        default_factory=list,
        description="当前轮返回的最终结果。",
    )
    # analysis agents
    document_reader_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="文档阅读的历史",
    )
    analyst_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="analyst过去获得的信息和进行的分析",
    )

