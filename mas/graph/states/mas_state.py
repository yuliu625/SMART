"""

"""

from langchain_core.messages import AnyMessage
from typing import TypedDict, Any
from pydantic import BaseModel, Field

from langchain_core.documents import Document


class MASState(BaseModel):
    original_pdf_text: str = Field(
        description="原始的pdf文档的text。专门用一个字段是为了避免和current_message出现问题。",
    )
    # current related, 整个MAS控制相关。
    current_agent_name: str = Field(
        default="arbiter",
        description="当前执行操作的agent的名字",
    )
    current_message: str = Field(
        default="",
        description="调用当前agent的上一个agent传递的信息。",
    )
    more_information: bool = Field(
        default=False,
        description="analyst选择是否需要进一步的分析。",
    )
    # validator related
    # # 剩余验证步骤，如果用完，就必须交给arbiter进行最终仲裁。
    remaining_validation_rounds: int = Field(
        default=5,
        description="validator剩余可进行验证的次数。",
    )
    remaining_retrieve_rounds: int = Field(
        default=5,
        description="analyst剩余可以进行查询次数。"
    )
    # # validator要求analysis模块要进行重新分析的{agent: content}。
    is_need_verification: bool = Field(
        default=False,
        description="validator决定是否需要analyst进一步分析。",
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
    arbiter_decision: list[AnyMessage] = Field(
        default_factory=list,
        description="arbiter进行最终的仲裁的分析内容。",
    )
    # rag and analyst
    # # control
    control_last_round_result_number: int = Field(
        default=-1,
        description="上轮获取的结果的数量",
    )
    control_query_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="query重写使用。查询的历史，用于rag中的agent进行对话。",
    )
    control_query_result_history: list[Document] = Field(
        default_factory=list,
        description="历史查询的结果，返回新查询结果是用于去重。",
    )
    # # query result
    control_current_query_results: list[Document] = Field(
        default_factory=list,
        description="当前轮返回的最终结果。",
    )
    # analysis agents
    control_document_reader_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="文档阅读的历史",
    )
    control_analyst_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="analyst过去获得的信息和进行的分析",
    )
    # # financial
    financial_last_round_result_number: int = Field(
        default=-1,
        description="上轮获取的结果的数量",
    )
    financial_query_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="query重写使用。查询的历史，用于rag中的agent进行对话。",
    )
    financial_query_result_history: list[Document] = Field(
        default_factory=list,
        description="历史查询的结果，返回新查询结果是用于去重。",
    )
    # # query result
    financial_current_query_results: list[Document] = Field(
        default_factory=list,
        description="当前轮返回的最终结果。",
    )
    # analysis agents
    financial_document_reader_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="文档阅读的历史",
    )
    financial_analyst_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="analyst过去获得的信息和进行的分析",
    )
    # # strategic
    strategic_last_round_result_number: int = Field(
        default=-1,
        description="上轮获取的结果的数量",
    )
    strategic_query_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="query重写使用。查询的历史，用于rag中的agent进行对话。",
    )
    strategic_query_result_history: list[Document] = Field(
        default_factory=list,
        description="历史查询的结果，返回新查询结果是用于去重。",
    )
    # # query result
    strategic_current_query_results: list[Document] = Field(
        default_factory=list,
        description="当前轮返回的最终结果。",
    )
    # analysis agents
    strategic_document_reader_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="文档阅读的历史",
    )
    strategic_analyst_chat_history: list[AnyMessage] = Field(
        default_factory=list,
        description="analyst过去获得的信息和进行的分析",
    )

