"""

"""

from __future__ import annotations
import pytest

from typing import TYPE_CHECKING
# if TYPE_CHECKING:

from mas.nodes import AgentFactory


def test_arbiter_1():
    agent_factory = AgentFactory()
    arbiter = agent_factory.get_arbiter()


if __name__ == '__main__':
    test_arbiter_1()
