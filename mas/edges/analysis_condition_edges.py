"""
分析模块会使用的条件边。
"""

from __future__ import annotations

from mas.schemas.final_mas_state import MASState

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def is_need_more_information(
    state: MASState,
) -> bool:
    ...

