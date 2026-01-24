"""
对于当前MAS的IO方法。

针对mas.schemas中的定义。
"""

from __future__ import annotations
from loguru import logger

from mas.schemas.single_agent_mas_state import SingleAgentMASState
from mas.schemas.sequential_mas_state import SequentialMASState
from mas.schemas.final_mas_state import FinalMASState
# from rag.loading.load_text import TextLoadingMethods
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from pathlib import Path
import json
from langchain_core.messages import (
    messages_to_dict,
    messages_from_dict,
)
from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class IOMethods:
    @staticmethod
    def load_single_agent_mas_state(
        markdown_file_path: str | Path,
    ) -> SingleAgentMASState:
        # 处理路径。
        markdown_file_path = Path(markdown_file_path)
        # 读取文本。
        markdown_text = markdown_file_path.read_text(encoding='utf-8')
        # 构造state。
        single_agent_state = SingleAgentMASState(
            decision_shared_messages=[
                HumanMessage(content=markdown_text),
            ],
        )
        logger.trace(f"\nLoaded SingleAgentState: \n{single_agent_state}")
        return single_agent_state

    @staticmethod
    def save_single_agent_mas_state(
        state: SingleAgentMASState,
        result_path: str | Path,
    ) -> SingleAgentMASState:
        # 处理路径。
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # 读取结果。
        result = dict(
            decision_shared_messages=messages_to_dict(
                messages=state['decision_shared_messages'],
            ),
            final_decision=state['final_decision'].model_dump(),
        )
        # logger.debug(f"Type of result: {type(result)}")
        # logger.debug(f"Type of final_decision: {type(result['final_decision'])}")
        logger.trace(f"\nSingleAgentState to save: \n{result}")
        # 执行保存。
        result_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=4),
            encoding='utf-8',
        )
        logger.success(f"\nSaved SingleAgentState: \n{result}")
        return state

    @staticmethod
    def load_sequential_mas_state(
        markdown_file_path: str | Path,
        general_query_path: str | Path,
    ) -> SequentialMASState:
        # 处理路径。
        markdown_file_path = Path(markdown_file_path)
        general_query_path = Path(general_query_path)
        # 读取文本。
        markdown_text = markdown_file_path.read_text(encoding='utf-8')
        query_text = PromptTemplateLoader.load_human_message_prompt_template_from_j2(
            human_message_prompt_template_path=general_query_path,
        ).format().content
        # 构造state。
        sequential_workflow_state = SequentialMASState(
            original_pdf_text=markdown_text,
            current_message=query_text,
        )
        logger.trace(f"\nLoaded SequentialWorkflowState: \n{sequential_workflow_state}")
        return sequential_workflow_state

    @staticmethod
    def save_sequential_mas_state(
        state: SequentialMASState,
        result_path: str | Path,
    ) -> SequentialMASState:
        # 处理路径。
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # 读取结果。
        result = dict(
            decision_shared_messages=messages_to_dict(
                messages=state['decision_shared_messages'],
            ),
            final_decision=state['final_decision'].model_dump(),
        )
        # logger.debug(f"Type of result: {type(result)}")
        # logger.debug(f"Type of final_decision: {type(result['final_decision'])}")
        logger.trace(f"\nSequentialWorkflowState to save: \n{result}")
        # 执行保存。
        result_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=4),
            encoding='utf-8',
        )
        logger.success(f"\nSaved SequentialWorkflowState: \n{result}")
        return state

    @staticmethod
    def load_final_mas_state(

    ) -> FinalMASState:
        raise NotImplementedError

    @staticmethod
    def save_final_mas_state(

    ) -> FinalMASState:
        raise NotImplementedError

