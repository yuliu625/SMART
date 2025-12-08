"""

"""

from __future__ import annotations

from mas.schemas import MASState

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def is_final_round(state: MASState) -> bool:
    if state.remaining_validation_rounds == 0:
        return True
    else:
        return False

