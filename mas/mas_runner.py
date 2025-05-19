"""

"""

from .graph import MASGraphBuilder
from .utils import (
    VectorStoreLoader,
    get_default_dir,
    load_txt,
)

from pathlib import Path


class MASRunner:
    """
    MAS运行工具。

    使用策略模式，封装所有加载和运行过程。
    因为这个类已经是高层对外暴露的，我不使用函数式编程。
    """
    def __init__(
        self,
        base_dir: str,
        pdf_name: str,
        modality: str,
        loading_method: str,
        embedding_method: str,
    ):
        # self.base_dir = base_dir
        self.pdf_name = pdf_name
        self.modality = modality
        self.loading_method = loading_method
        self.embedding_method = embedding_method

        self.default_dir = get_default_dir(base_dir)
        self.vector_store = self.get_vector_store()
        self.mas_graph = self.get_mas_graph()

    def run(self):
        original_pdf_text = self.get_original_pdf_text()
        result = self.mas_graph.invoke({'original_pdf_text': original_pdf_text})
        return result

    def get_mas_graph(self):
        mas_graph_builder = MASGraphBuilder(
            vector_store=self.vector_store,
            pdf_name=self.pdf_name,
        )
        mas_graph = mas_graph_builder.build_graph()
        return mas_graph

    def get_vector_store(self):
        vector_store_loader = VectorStoreLoader(base_dir=self.default_dir.base_dir)
        vector_store = vector_store_loader.get_vector_store(
            modality=self.modality,
            loading_method=self.loading_method,
            embedding_method=self.embedding_method,
        )
        return vector_store

    def get_original_pdf_text(self) -> str:
        txt_path = self.default_dir.txt_pdf_dir / 'vlm' / f"{self.pdf_name}.txt"
        text = load_txt(txt_path)
        return text

