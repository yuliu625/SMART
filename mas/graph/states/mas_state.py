"""

"""

from langchain_core.messages import AnyMessage
from typing import TypedDict, Any
from pydantic import BaseModel, Field

from langchain_core.documents import Document


class MASState(BaseModel):
    # rag
    query_chat_history: list[Any] = Field(
        default_factory=list,
        description="查询的历史，用于rag中的agent进行对话。",
    )
    # # result history
    query_result_history: list[Document] = Field(
        default_factory=list,
        description="历史查询的结果，返回新查询结果是用于去重。",
    )
    current_query: str = Field(
        description="当前的查询。",
    )
    last_round_result_number: int = Field(
        default=-1,
        description="上轮获取的结果的数量",
    )
    # # query result
    current_query_results: list[Document] = Field(
        default_factory=list,
        description="当前轮返回的最终结果。",
    )
    # analysis agents
    document_reader_history: list[AnyMessage] = Field(
        default_factory=list,
        description="文档阅读的历史",
    )
    more_information: bool = Field(
        default=False,
        description="analyst选择是否需要进一步的分析。",
    )
    analyst_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="analyst过去获得的信息和进行的分析",
    )
    # decision agents
    recognizer_history: list[AnyMessage] = Field(
        default_factory=list,
        description="",
    )
    validator_history: list[AnyMessage] = Field(
        default_factory=list,
        description="",
    )
    arbiter_decision: list[AnyMessage] = Field(
        default_factory=list,
        description="",
    )
    # validator related
    # # 剩余验证步骤，如果用完，就必须交给arbiter进行最终仲裁。
    remaining_validation_rounds: int = Field(
        default=3,
        description="",
    )
    # # validator要求analysis模块要进行重新分析的{agent: content}。
    is_need_verification: bool = Field(
        default=False,
        description="",
    )
    verification_requests: dict[str, str] = Field(
        default_factory=dict,
        description=""
    )
