"""
分析子图使用的state。
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.documents import Document
    from langchain_core.messages import AnyMessage


class AnalysisState(BaseModel):
    current_agent_name: str = Field(
        default="arbiter",
        description="当前执行操作的agent的名字",
    )
    current_message: str = Field(
        default="",
        description="调用当前agent的上一个agent传递的信息。",
    )
    is_need_more_information: bool = Field(
        default=False,
        description="analyst选择是否需要进一步的分析。",
    )
    remaining_retrieve_rounds: int = Field(
        default=5,
        description="analyst剩余可以进行查询次数。"
    )
    document_reader_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="文档阅读的历史",
    )
    analyst_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="analyst过去获得的信息和进行的分析",
    )

