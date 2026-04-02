"""
for multi-agent debate graph state.
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.documents import Document
from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class MultiAgentDebateState(BaseModel):
    """
    state of multi-agent debate graph
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

    # Analysis Module
    ## 在这种 pattern 下，analysis module 中的 agent 没有独立的记忆控制，所有 agent 共享记忆池。

    # RAG
    ## 检索结果/当前analyst可以进行分析的材料。
    current_documents: list[Document] = Field(
        default_factory=list,
        description="RAG 模块返回的结果。",
    )
    raise NotImplementedError

