"""
Tests for information merger.
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.agent_nodes.analysis_agents.information_merger import InformationMerger
from mas.schemas.sequential_mas_state import SequentialMASState

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.documents import Document
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_test_information_merger() -> InformationMerger:
    information_merger = InformationMerger()
    return information_merger


def make_test_sequential_workflow_state() -> SequentialMASState:
    state = SequentialMASState(
        original_pdf_text=Path(
            r"D:\dataset\smart\tests\docling_1\000004.md"
        ).read_text(encoding='utf-8'),
        decision_shared_messages=[
            HumanMessage(content="<!--surveyor-start-->I am surveyor's result!<!--surveyor-end-->"),
        ],
        current_message="I am a query.",
        current_documents=[
            Document(page_content="Document result 1."),
            Document(page_content="Document result 2."),
            Document(page_content="Document result 3."),
        ],
        current_agent_name='analyst',
        last_agent_name='rag',
    )
    return state


class TestInformationMerger:
    @pytest.mark.parametrize(
        "information_merger, state", [
        (make_test_information_merger(),
         make_test_sequential_workflow_state()),
    ])
    @pytest.mark.asyncio
    async def test_information_merger_as_node_in_final_mas(
        self,
        information_merger: InformationMerger,
        state: SequentialMASState,
    ):
        logger.trace(f"\nTest State: \n{state}")
        result = await information_merger.process_state(
            state=state,
            config=None,
        )
        logger.info(f"\nInformation Merger Result: \n{result}")

