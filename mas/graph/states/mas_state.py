"""

"""

from langchain_core.messages import AnyMessage
from typing import TypedDict, Any
from pydantic import BaseModel, Field


class MASState(BaseModel):
    messages: list[AnyMessage] = []
    # analysis agents

    # decision agents
    recognizer_history: list[AnyMessage] = []
    validator_history: list[AnyMessage] = []
    arbiter_decision: list[AnyMessage] = []
    # validator related
    # # 剩余验证步骤，如果用完，就必须交给arbiter进行最终仲裁。
    remaining_validation_rounds: int = 3
    # # validator要求analysis模块要进行重新分析的{agent: content}。
    is_need_verification: bool = False
    verification_requests: dict[str, str]
