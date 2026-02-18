"""
对于当前MAS的IO方法。

针对mas.schemas中的定义。
"""

from __future__ import annotations
from loguru import logger

from mas.schemas.single_agent_state import SingleAgentState
from mas.schemas.sequential_workflow_state import SequentialWorkflowState
from mas.schemas.final_mas_state import FinalMASState
# from rag.loading.load_text import TextLoadingMethods
from mas.prompts.prompt_template_loader import PromptTemplateLoader
from mas.utils.content_annotator import ContentAnnotator

from pathlib import Path
import json
from langchain_core.messages import (
    messages_to_dict,
    messages_from_dict,
)
from langchain_core.messages import HumanMessage

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class CachedIOMethods:
    @staticmethod
    def load_cached_single_agent_state(
        surveyor_cache_path: str | Path,
    ) -> SingleAgentState:
        # 处理路径。
        surveyor_cache_path = Path(surveyor_cache_path)
        # 读取文本。
        surveyor_content = surveyor_cache_path.read_text(encoding='utf-8')
        # 构造state。
        single_agent_state = SingleAgentState(
            decision_shared_messages=[
                HumanMessage(content=surveyor_content),
            ],
        )
        logger.trace(f"\nLoaded cached SingleAgentState: \n{single_agent_state}")
        return single_agent_state

    @staticmethod
    def save_cached_single_agent_state(
        state: SingleAgentState,
        result_path: str | Path,
    ) -> SingleAgentState:
        # 处理路径。
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # 读取结果。
        result = dict(
            decision_shared_messages=messages_to_dict(
                messages=state.decision_shared_messages#['decision_shared_messages'],
            ),
            final_decision=state.final_decision#['final_decision'],#.model_dump(),
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
    def load_cached_sequential_workflow_state(
        surveyor_cache_path: str | Path,
        general_query_path: str | Path,
    ) -> SequentialWorkflowState:
        # 处理路径。
        surveyor_cache_path = Path(surveyor_cache_path)
        general_query_path = Path(general_query_path)
        # 读取文本。
        surveyor_content = surveyor_cache_path.read_text(encoding='utf-8')
        query_text = PromptTemplateLoader.load_human_message_prompt_template_from_j2(
            human_message_prompt_template_path=general_query_path,
        ).format().content
        # 构造state。
        sequential_workflow_state = SequentialWorkflowState(
            original_pdf_text="",
            current_message=query_text,
            decision_shared_messages=[
                HumanMessage(
                    content=ContentAnnotator.annotate_with_html_comment(
                        tag='surveyor',
                        original_text=surveyor_content,
                    ),
                ),
            ],
        )
        logger.trace(f"\nLoaded Cached SequentialWorkflowState: \n{sequential_workflow_state}")
        return sequential_workflow_state

    @staticmethod
    def save_cached_sequential_workflow_state(
        state: SequentialWorkflowState,
        result_path: str | Path,
    ) -> SequentialWorkflowState:
        # 处理路径。
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # 读取结果。
        result = dict(
            decision_shared_messages=messages_to_dict(
                messages=state['decision_shared_messages'],
            ),
            final_decision=state['final_decision'],#.model_dump(),
        )
        # logger.debug(f"Type of result: {type(result)}")
        # logger.debug(f"Type of final_decision: {type(result['final_decision'])}")
        logger.trace(f"\nCached SequentialWorkflowState to save: \n{result}")
        # 执行保存。
        result_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=4),
            encoding='utf-8',
        )
        logger.success(f"\nSaved Cached SequentialWorkflowState: \n{result}")
        return state

    @staticmethod
    def load_cached_final_mas_state(
        surveyor_cache_path: str | Path,
    ) -> FinalMASState:
        # 处理路径。
        surveyor_cache_path = Path(surveyor_cache_path)
        # 读取文本。
        surveyor_content = surveyor_cache_path.read_text(encoding='utf-8')
        # 构造state。
        final_mas_state = FinalMASState(
            original_pdf_text="",
            decision_shared_messages=[
                HumanMessage(
                    content=ContentAnnotator.annotate_with_html_comment(
                        tag='surveyor',
                        original_text=surveyor_content,
                    ),
                ),
            ],
        )
        logger.trace(f"\nLoaded Cached FinalMASState: \n{final_mas_state}")
        return final_mas_state

    @staticmethod
    def save_cached_final_mas_state(
        state: FinalMASState,
        result_path: str | Path,
    ) -> FinalMASState:
        # 处理路径。
        result_path = Path(result_path)
        result_path.parent.mkdir(parents=True, exist_ok=True)
        # 读取结果。
        result = dict(
            analysis_process_history=[
                messages_to_dict(messages=analysis_process,)
                for analysis_process in state['analysis_process_history']
            ],
            decision_shared_messages=messages_to_dict(
                messages=state['decision_shared_messages'],
            ),
            final_decision=state['final_decision'],#.model_dump(),
        )
        # logger.debug(f"Type of result: {type(result)}")
        # logger.debug(f"Type of final_decision: {type(result['final_decision'])}")
        logger.trace(f"\nFinalMASState to save: \n{result}")
        # 执行保存。
        result_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=4),
            encoding='utf-8',
        )
        logger.success(f"\nSaved Cached FinalMASState: \n{result}")
        return state

