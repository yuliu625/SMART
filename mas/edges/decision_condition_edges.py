"""
决策模块会使用的条件边。
"""

from __future__ import annotations

from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING, Literal, cast
# if TYPE_CHECKING:


# ==== for investigator ====
def is_need_validation(
    state: FinalMASState,
) -> Literal['analyst', 'adjudicator']:
    """
    通过直接读取下一个investigator请求的agent，获得下一个agent的路由信息。

    Args:
        state:

    Returns:
        Literal['analyst', 'adjudicator']: 下一个agent的名字。
    """
    current_agent_name = state.current_agent_name
    # assert current_agent_name in ('analyst', 'adjudicator')
    current_agent_name = cast(Literal['analyst', 'adjudicator'], current_agent_name)
    return current_agent_name

