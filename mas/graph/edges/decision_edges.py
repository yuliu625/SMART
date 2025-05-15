"""

"""

from ..states import MASState

from langgraph.graph.graph import END

from typing import Literal


def condition_final_round(state: MASState) -> Literal[END, 'recognizer']:
    if state.remaining_validation_rounds == 0:
        return END
    else:
        return 'recognizer'
