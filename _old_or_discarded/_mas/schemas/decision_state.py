"""
决策子图使用的state。
"""

from __future__ import annotations
from pydantic import BaseModel, Field

from langchain_core.messages import AnyMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class DecisionState(BaseModel):
    # MAS共有
    current_agent_name: str = Field(
        description="",
    )
    current_message: str = Field(
        description="",
    )

    # 初始。
    # # recognizer看到的初始文本内容。
    original_pdf_text: str = Field(
        description="原始的pdf文档的text。专门用一个字段是为了避免和current_message出现问题。",
    )

    # 控制。
    # # 剩余验证步骤，如果用完，就必须交给arbiter进行最终仲裁。
    remaining_validation_rounds: int = Field(
        default=5,
        description="validator剩余可进行验证的次数。",
    )

    # agents相关。
    # # decision agents
    shared_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="共有的记忆。",
    )
    # recognizer_chat_history: list[AnyMessage] = Field(
    #     default_factory=list,
    #     description="recognizer通过长文本进行全面的判断",
    # )
    # validator_chat_history: list[AnyMessage] = Field(
    #     default_factory=list,
    #     description="validator进行各种验证的记录。",
    # )
    arbiter_decision: dict = Field(
        default_factory=dict,
        description="arbiter的结构化输出。",
    )

