"""

"""

from typing import TypedDict, Any


class State(TypedDict):
    messages: list[Any]
    # analysis agents
    
    # decision agents
    recognizer_messages: list[Any]
    validator_messages: list[Any]
    arbiter_messages: list[Any]
