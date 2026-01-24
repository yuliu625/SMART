"""
测试surveyor。
"""

from __future__ import annotations
import pytest
from loguru import logger

# from mas.agent_nodes.agent_factory import AgentFactory
from mas.agent_nodes.decision_agents.surveyor import Surveyor
from mas.schemas.final_mas_state import FinalMASState
from mas.schemas.sequential_mas_state import SequentialMASState
# from mas.models.local_llm_factory import LocalLLMFactory
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage
from pathlib import Path

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
                system_message_prompt_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2",
            ).format()
        ),
    )
    return surveyor


def make_test_sequential_workflow_state() -> SequentialMASState:
    state = SequentialMASState(
        current_agent_name='surveyor',
        last_agent_name='start',
        original_pdf_text=Path(
            r"D:\dataset\smart\tests\docling_1\000004.md"
        ).read_text(encoding='utf-8'),
    )
    return state


def make_test_final_mas_state() -> FinalMASState:
    state = FinalMASState(
        current_agent_name='surveyor',
        last_agent_name='start',
        original_pdf_text=Path(
            r"D:\dataset\smart\tests\docling_1\000004.md"
        ).read_text(encoding='utf-8'),
    )
    return state


class TestSurveyor:
    @pytest.mark.parametrize(
        "surveyor, state", [
        (make_test_surveyor(),
         make_test_final_mas_state()),
    ])
    @pytest.mark.asyncio
    async def test_surveyor_as_node_in_final_mas(
        self,
        surveyor: Surveyor,
        state: FinalMASState,
    ):
        logger.trace(f"\nTest State: \n{state}")
        result = await surveyor.process_state(
            state=state,
            config=None,
        )
        logger.info(f"\nSurveyor Result: \n{result}")

    @pytest.mark.parametrize(
        "surveyor, state", [
        (make_test_surveyor(),
         make_test_sequential_workflow_state()),
    ])
    @pytest.mark.asyncio
    async def test_surveyor_as_node_in_final_mas(
        self,
        surveyor: Surveyor,
        state: SequentialMASState,
    ):
        logger.trace(f"\nTest State: \n{state}")
        result = await surveyor.process_state(
            state=state,
            config=None,
        )
        logger.info(f"\nSurveyor Result: \n{result}")

