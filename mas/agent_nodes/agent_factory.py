"""
构建各个作为agent的node。
"""

from __future__ import annotations

from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.agent_nodes.decision_agents.investigator import Investigator
from mas.agent_nodes.decision_agents.adjudicator import Adjudicator
from mas.agent_nodes.analysis_agents.analyst import Analyst

from typing import TYPE_CHECKING, Literal
if TYPE_CHECKING:
    from mas.agent_nodes.base_agent import BaseAgent


class AgentFactory:
    @staticmethod
    def create_agent(
        agent_type: Literal[
            'surveyor', 'investigator', 'adjudicator',
            'analyst', 'rag_agent',
        ],
    ) -> BaseAgent:
        ...

    @staticmethod
    def create_surveyor(

    ) -> BaseAgent:
        ...

    @staticmethod
    def create_investigator(

    ) -> BaseAgent:
        ...

    @staticmethod
    def create_adjudicator(

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

