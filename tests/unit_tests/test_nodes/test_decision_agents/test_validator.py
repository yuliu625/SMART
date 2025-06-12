"""

"""


from __future__ import annotations
import pytest

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from mas.nodes import AgentFactory


def test_validator_1():
    agent_factory = AgentFactory()
    validator = agent_factory.get_validator()


if __name__ == '__main__':
    test_validator_1()
