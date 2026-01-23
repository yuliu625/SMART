"""
分析模块会使用的条件边。
"""

from __future__ import annotations

from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING, Literal, cast
# if TYPE_CHECKING:


# ==== for analyst ====
def is_need_more_information(
    state: FinalMASState,
) -> Literal['rag', 'investigation']:
    """
    通过直接读取下一个investigator请求的agent，获得下一个agent的路由信息。

    Args:
        state:

    Returns:
        Literal['rag', 'investigation']: 下一个agent的名字。
    """
    current_agent_name = state.current_agent_name
    # assert current_agent_name in ('rag', 'investigation')
    current_agent_name = cast(Literal['rag', 'investigation'], current_agent_name)
    return current_agent_name

