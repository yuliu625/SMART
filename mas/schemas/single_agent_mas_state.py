"""
仅单独agent的graph。
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class SingleAgentMASState(BaseModel):
    """
    Single agent中使用的state。

    实际等同:
        - 整个系统运行需要的最小必要字段。
        - Adjudicator需要的字段。
    """
    # MAS条件控制。
    ## current related, 为兼容性保留。
    ## 在这个实现中，实际不进行任何执行。
    current_agent_name: str = Field(
        default="adjudicator",
        description="当前应该运行的agent的名字。",
    )
    last_agent_name: str = Field(
        default="start",
        description="上一个agent的名字，用于追寻任务和请求的来源。",
    )
    current_message: str = Field(
        default="",
        description="当前agent可能会使用的信息。",
    )

    # Decision Module
    ## 共用字段。该实现需要额外处理进行初始化以启动系统。
    decision_shared_messages: list[AnyMessage] = Field(
        default_factory=list,
        description="所有decision中的agent共用的messages。在这个实现中，时adjudicator专用。使用需要额外处理。",
    )
    ### Adjudicator. 代表最终结果的重要字段。
    final_decision: dict = Field(
        default_factory=dict,
        description="Adjudicator结构化输出的最终决策。",
    )

