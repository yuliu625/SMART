"""
决策模块会使用的条件边。
"""

from __future__ import annotations

from mas.schemas.final_mas_state import FinalMASState

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


def is_need_validation(
    state: FinalMASState,
) -> bool:
    ...


def get_next_agent_name(
    state: FinalMASState,
) -> Literal['investigator', 'analyst']:
    ...


