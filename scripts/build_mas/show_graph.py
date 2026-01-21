"""
可视化检查当前计算图的方法。
"""

from __future__ import annotations
from loguru import logger

from mas.mas_factory import MASFactory
from mas.utils.graph_visualizer import GraphVisualizer

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from langgraph.graph.state import CompiledStateGraph


def show_single_agent_mas_graph():
    # HARDCODED: 仅构建，并不实际运行MAS。
    mas = MASFactory.create_single_agent_mas_via_ollama(
        adjudicator_main_llm_model_name='qwen2.5:1.5b',
        adjudicator_main_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_main_llm_system_prompt_template.j2',
        adjudicator_formatter_llm_model_name='qwen2.5:1.5b',
        adjudicator_formatter_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\single_agent_mas\adjudicator_formatter_llm_system_prompt_template.j2',
    )
    mermaid_code = GraphVisualizer.get_mermaid_code(
        graph=mas,
    )
    logger.info(f"\nMermaid Code: \n{mermaid_code}")


def main(

):
    ...


if __name__ == '__main__':
    show_single_agent_mas_graph()

