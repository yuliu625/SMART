"""
可视化检查当前计算图的方法。
"""

from __future__ import annotations
from loguru import logger

from mas.mas_factory import MASFactory
from mas.rag_factory import RagFactory
# from mas.rag_nodes.chroma_rag_builder import ChromaRAGBuilder
from mas.utils.graph_visualizer import GraphVisualizer
from rag.storing.chroma_vector_store_builder import ChromaVectorStoreBuilder
# from rag.embedding.embedding_model_factory import EmbeddingModelFactory

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


def show_sequential_mas_graph():
    ...


def show_final_mas_graph():
    # HARDCODED: 仅构建，并不实际运行MAS。
    mas = MASFactory.create_final_mas_via_ollama(
        # surveyor
        surveyor_main_llm_model_name='qwen2.5:1.5b',
        surveyor_main_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\final_mas\surveyor_main_llm_system_prompt_template.j2',
        # investigator
        investigator_main_llm_model_name='qwen2.5:1.5b',
        investigator_main_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_main_llm_system_prompt_template.j2',
        investigator_formatter_llm_model_name='qwen2.5:1.5b',
        investigator_formatter_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\final_mas\investigator_formatter_llm_system_prompt_template.j2',
        # adjudicator
        adjudicator_main_llm_model_name='qwen2.5:1.5b',
        adjudicator_main_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_main_llm_system_prompt_template.j2',
        adjudicator_formatter_llm_model_name='qwen2.5:1.5b',
        adjudicator_formatter_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\final_mas\adjudicator_formatter_llm_system_prompt_template.j2',
        # analyst
        analyst_main_llm_model_name='qwen2.5:1.5b',
        analyst_main_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_main_llm_system_prompt_template.j2',
        analyst_formatter_llm_model_name='qwen2.5:1.5b',
        analyst_formatter_llm_system_message_template_path=r'D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_formatter_llm_system_prompt_template.j2',
        rag=RagFactory.create_simple_rag_via_ollama(
            vector_store_persist_directory=r"D:\dataset\smart\tests\t_vector_store",
            embedding_model_model_name='nomic-embed-text',
            embedding_model_num_ctx=8192,
            search_configs={},
        )
    )
    mermaid_code = GraphVisualizer.get_mermaid_code(
        graph=mas,
    )
    logger.info(f"\nMermaid Code: \n{mermaid_code}")


def main(

):
    ...


if __name__ == '__main__':
    # show_single_agent_mas_graph()
    show_final_mas_graph()

