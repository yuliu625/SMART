"""
Sequential Workflow State

State definition of sequential mas.
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class SequentialMasState(BaseModel):
    """
    Sequential MAS中使用的state。

    实际等同:
        - 在有RAG支持下的最小必要字段。
        -   Decision::Surveyor,Adjudicator,
            Analysis::Analyst,
            RAG::Retriever
            需要的字段。
    """
    # 共用字段。该实现需要额外处理。
    decision_shared_messages: list[AnyMessage] = Field(
        default_factory=list,
        description="所有decision中的agent共用的messages。在这个实现中，时adjudicator专用。使用需要额外处理。",
    )
    # Adjudicator
    final_decision: dict = Field(
        default_factory=dict,
        description="Adjudicator结构化输出的最终决策。",
    )
    # 为兼容性保留。实际不进行任何执行。
    current_message: str = Field(
        default="",
        description="调用当前agent的上一个agent传递的信息。",
    )

