"""
构建各个作为agent的node。
"""

from __future__ import annotations

from mas.agent_nodes.decision_agents.surveyor import Surveyor

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mas.agent_nodes.base_agent import BaseAgent


class AgentFactory:
    @staticmethod
    def create_agent(

    ) -> BaseAgent:
        ...

    @staticmethod
    def create_recognizer(

    ) -> BaseAgent:
        ...

    @staticmethod
    def create_validator(

    ) -> BaseAgent:
        ...

    @staticmethod
    def create_arbiter(

    ) -> BaseAgent:
        ...

    @staticmethod
    def create_analyst(

    ) -> BaseAgent:
        ...

    @staticmethod
    def create_rag_agent(

    ) -> BaseAgent:
        ...

