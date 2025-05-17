"""

"""

from .graph import MASGraphBuilder
from .utils import VectorStoreLoader, get_default_dir

from pathlib import Path


class MASRunner:
    """
    MAS运行工具。

    使用策略模式，封装所有加载和运行过程。
    """
    def __init__(
        self,
        base_dir: str,
        pdf_name: str,
        modality: str,
        loading_method: str,
        embedding_method: str,
    ):
        self.base_dir = base_dir
        self.pdf_name = pdf_name
        self.modality = modality
        self.loading_method = loading_method
        self.embedding_method = embedding_method

        self.default_dir = get_default_dir(base_dir)

    def run(self):
        ...

    def get_mas_graph(
        self,
        vector_store,
        pdf_name: str,
    ):
        mas_graph_builder = MASGraphBuilder(
            vector_store=vector_store,
            pdf_name=pdf_name,
        )
        mas_graph = mas_graph_builder.build_graph()
        return mas_graph

    def get_vector_store(
        self,
        base_dir: str,
        modality: str,
        loading_method: str,
        embedding_method: str,
    ):
        vector_store_loader = VectorStoreLoader(base_dir=base_dir)
        vector_store = vector_store_loader.get_vector_store(
            modality=modality,
            loading_method=loading_method,
            embedding_method=embedding_method,
        )
        return vector_store

    def get_original_pdf_text(
        self,
        base_dir: Path,
        pdf_name: str,
    ) -> str:
        ...

