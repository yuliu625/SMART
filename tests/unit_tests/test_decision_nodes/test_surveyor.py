"""
测试surveyor。
"""

from __future__ import annotations
import pytest
from loguru import logger

# from mas.agent_nodes.agent_factory import AgentFactory
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.schemas.final_mas_state import FinalMASState
# from mas.models.local_llm_factory import LocalLLMFactory
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage

from typing import TYPE_CHECKING,cast
# if TYPE_CHECKING:
#     from mas.agent_nodes.decision_agents.surveyor import Surveyor


def make_test_surveyor() -> Surveyor:
    surveyor = Surveyor(
        main_llm=ChatOllama(
            model='qwen2.5:1.5b',
            temperature=0.7,
        ),
        main_llm_system_message=cast(
            SystemMessage,
            PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                system_message_prompt_template_path=r"",
            ).format()
        ),
    )
    return surveyor


def make_test_state() -> FinalMASState:
    ...


class TestSurveyor:
    @pytest.mark.parametrize(
        "surveyor, state", [
        (make_test_surveyor(),
         make_test_state()),
    ])
    @pytest.mark.asyncio
    async def test_surveyor(
        self,
        surveyor: Surveyor,
        state: FinalMASState,
    ):
        result = surveyor.process_state(
            state=state,
            config=None,
        )
        logger.info(f"\nSurveyor Result: \n{result}")

