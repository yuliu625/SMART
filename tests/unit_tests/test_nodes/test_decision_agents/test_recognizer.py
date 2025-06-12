"""

"""

from __future__ import annotations
import pytest

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from mas.schemas import MASState
from mas.nodes import AgentFactory


def test_recognizer_1():
    agent_factory = AgentFactory()
    recognizer = agent_factory.get_recognizer()
    result = recognizer.run(MASState(original_pdf_text=""))
    print(result)


if __name__ == '__main__':
    test_recognizer_1()
