"""
决策子图使用的state。
"""

from pydantic import BaseModel, Field
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langchain_core.messages import AnyMessage


class DecisionState(BaseModel):
    # recognizer看到的初始文本内容。
    original_pdf_text: str = Field(
        description="原始的pdf文档的text。专门用一个字段是为了避免和current_message出现问题。",
    )
    # # 剩余验证步骤，如果用完，就必须交给arbiter进行最终仲裁。
    remaining_validation_rounds: int = Field(
        default=5,
        description="validator剩余可进行验证的次数。",
    )
    # decision agents
    recognizer_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="recognizer通过长文本进行全面的判断",
    )
    validator_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="validator进行各种验证的记录。",
    )
    arbiter_context: list[str] = Field(
        default=list,
        description="累计的validator的对话记录。"
    )
    arbiter_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="arbiter进行最终的仲裁的分析内容。",
    )
    arbiter_decision: dict = Field(
        default_factory=dict,
        description="arbiter的结构化输出。"
    )


