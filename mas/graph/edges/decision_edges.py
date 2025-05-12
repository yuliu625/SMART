"""

"""

from langgraph.graph.graph import (
    END,
    START,
)

from typing import Literal


def condition_final_round(state) -> Literal[END, 'recognizer']:
    if state.remaining_validation_rounds == 0:
        return END
    else:
        return 'recognizer'
