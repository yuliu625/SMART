"""
独立构建 benchmark 的结果。
"""

from __future__ import annotations
import asyncio
from loguru import logger

from mas.schemas.structured_output_format import (
    AdjudicatorDecision,
)
from mas.schemas.single_agent_state import SingleAgentState
from mas.cached_io_methods import (
    CachedIOMethods,
)

from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from pathlib import Path
import os

from typing import TYPE_CHECKING, cast
if TYPE_CHECKING:
    from langchain_core.language_models import BaseChatModel
    from pydantic import BaseModel


def build_structured_llm(
    llm: BaseChatModel,
    schema_pydantic_base_model: type[BaseModel],
    # system_message: SystemMessage,
    max_retries: int = 3,
) -> BaseChatModel:
    """
    构造structured_llm的方法。

    这个实现默认:
        - 不对于system-message进行限制，不将system-message与llm提前绑定。
            - 但相关控制需要使用structured_llm的方法实现。

    Args:
        llm (BaseChatModel): 基础的用于推理的基座模型。需要具有结构化提取功能。
        schema_pydantic_base_model (BaseModel): 基于pydantic定义的schema。
        max_retries (int): 最大重试次数。基于runnable本身的实现。

    Returns:
        BaseChatModel: 被限制为仅会进行结构化输出的structured_llm。
    """
    structured_llm = llm.with_structured_output(
        schema=schema_pydantic_base_model,
    ).with_retry(
        stop_after_attempt=max_retries,
    )
    structured_llm = cast('BaseChatModel', structured_llm)
    return structured_llm


async def aget_structured_output(
    raw_str: str,
    structured_llm: BaseChatModel,
    formatter_system_message: SystemMessage,
) -> BaseModel:
    """
    提取结构化数据。用于条件判断和提取生成结果。

    States:
        _structured_llm (BaseChatModel): 构造好的可以进行结构化提取的llm。
        _formatter_system_message (SystemMessage): formatter_llm的指令。
    这里显式以调用的方法说明，以说明参与的对象。
    但structured_output应作为该类的内部必要方法，应该不需要外部设置。

    Args:
        raw_str (str): 原始LLM输出的字符串。
        structured_llm (BaseChatModel): 已经绑定了目标schema的llm。
        formatter_system_message (SystemMessage): 对formatter_llm的指令system-message。

    Returns:
        BaseModel: 基于初始定义schema的pydantic-base-model。
    """
    response = await structured_llm.ainvoke(
        input=[
            formatter_system_message,
            HumanMessage(raw_str),
        ],
    )
    return response


async def incremental_make_benchmark_results(
    # IO
    surveyor_cache_dir: str | Path,
    result_dir: str | Path,
    # MAS configurations
    formatter_llm_system_message_content: str,
) -> None:
    # path processing
    surveyor_cache_dir = Path(surveyor_cache_dir)
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    # build structured llm
    llm = ChatOpenAI(
        # HARDCODED
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        model='qwen-max',
        api_key=os.getenv("DASHSCOPE_API_KEY"),
    )
    structured_llm = build_structured_llm(
        llm=llm,
        schema_pydantic_base_model=AdjudicatorDecision,
        max_retries=3,
    )
    # run benchmark experiments
    surveyor_cache_path_list = list(surveyor_cache_dir.glob('*.txt'))
    for surveyor_cache_path in surveyor_cache_path_list:
        result_file_path = result_dir / f"{surveyor_cache_path.stem}.json"
        if result_file_path.exists():
            logger.info(f"Result file exists: {result_file_path}")
        else:
            surveyor_cache_content = surveyor_cache_path.read_text(encoding='utf-8')
            result = await aget_structured_output(
                raw_str=surveyor_cache_content,
                structured_llm=structured_llm,
                formatter_system_message=SystemMessage(
                    content=formatter_llm_system_message_content,
                )
            )
            # save result
            CachedIOMethods.save_cached_single_agent_state(
                state=SingleAgentState(
                    current_agent_name='end',
                    last_agent_name='adjudicator',
                    current_message="",
                    decision_shared_messages=[
                        AIMessage(content=surveyor_cache_content),
                    ],
                    final_decision=result.model_dump(),
                ),
                result_path=result_file_path,
            )
            logger.success(f"Save result: {result_file_path}")
    logger.success(f"All results saved in: {result_dir}")


async def main():
    # IO
    surveyor_cache_dir = r"D:\dataset\smart\data_pipeline_cache\surveyor_cache"
    result_dir = r"D:\dataset\smart\results\benchmark"
    # MAS configurations
    formatter_llm_system_message_content = """\
你是一个审计结论提取器。
请从裁判官（Adjudicator）的最终陈述中提取核心判定。
- 关键任务：提取风险是否存在（Boolean）、结论文本、置信度（Float）。
- 准则：仅提取文中明确给出的数值或立场。"""
    await incremental_make_benchmark_results(
        surveyor_cache_dir=surveyor_cache_dir,
        result_dir=result_dir,
        formatter_llm_system_message_content=formatter_llm_system_message_content,
    )


if __name__ == '__main__':
    asyncio.run(main())

