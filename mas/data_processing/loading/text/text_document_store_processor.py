"""

"""

from .text_processor import PymupdfTextLoader
from mas.models import YuFakeEmbeddingModel
from mas.data_processing import MetadataTools

from langchain_chroma import Chroma
from langchain_text_splitters import ExperimentalMarkdownSyntaxTextSplitter
from pathlib import Path

from langchain_core.documents import Document


class TextDocumentStoreProcessor:
    """

    """
    def __init__(
        self,
        text_document_store_dir: str | Path,
    ):
        self.text_document_store_dir = Path(text_document_store_dir)
        self.text_document_store_dir.mkdir(exist_ok=True, parents=True)

    def run(
        self,
        pdf_path: str | Path,
        loading_method: str,
    ) -> None:
        pdf_path = Path(pdf_path)
        documents = self.load_pdf(pdf_path=pdf_path, loading_method=loading_method)
        metadata = self.get_metadata(pdf_path=pdf_path)
        self.add_documents_to_vector_store(documents=documents, metadata=metadata, loading_method=loading_method)
        print(f"added text {pdf_path.name} to {self.text_document_store_dir / loading_method}")

    def load_pdf(
        self,
        pdf_path: str | Path,
        loading_method: str,
    ) -> list[Document]:
        pdf_loader = PymupdfTextLoader(pdf_path=pdf_path)
        documents = pdf_loader.run(loading_method=loading_method)
        documents = self._parse_markdown(documents=documents)
        return documents

    def get_metadata(
        self,
        pdf_path: str | Path,
    ) -> dict:
        pdf_path = Path(pdf_path)
        metadata_tools = MetadataTools()
        metadata = metadata_tools.get_text_metadata(pdf_path=pdf_path)
        return metadata

    def add_documents_to_vector_store(
        self,
        documents: list[Document],
        metadata: dict,
        loading_method: str,
    ) -> None:
        vector_store = Chroma(
            embedding_function=YuFakeEmbeddingModel(),
            persist_directory=str(self.text_document_store_dir / loading_method),
        )
        vector_store.add_texts(
            texts=[document.page_content for document in documents],
            metadatas=[metadata for _ in range(len(documents))],
        )

    def _parse_markdown(
        self,
        documents: list[Document],
    ) -> list[Document]:
        markdown_splitter = ExperimentalMarkdownSyntaxTextSplitter()
        result_documents = []
        for document in documents:
            result_documents += markdown_splitter.split_text(document.page_content)
        return result_documents

