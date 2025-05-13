"""

"""

from .text_document_store_processor import TextDocumentStoreProcessor
from mas.utils import get_default_dir

from pathlib import Path


class TextBatchProcessor:
    """

    """
    def __init__(
        self,
        base_dir: str,
    ):
        default_dir = get_default_dir(base_dir=base_dir)
        self.original_pdf_dir = default_dir.original_pdf_dir
        self.txt_pdf_dir = default_dir.txt_pdf_dir
        self.text_document_store_dir = default_dir.text_document_store_dir

    def batch_process(
        self,
        loading_methods: list[str],
    ):
        pdf_paths = self._get_pdf_paths(self.original_pdf_dir)
        for loading_method in loading_methods:
            for pdf_path in pdf_paths:
                self.run_a_processor(
                    text_document_store_dir=self.text_document_store_dir,
                    pdf_path=pdf_path,
                    loading_method=loading_method,
                )

    def run_a_processor(
        self,
        text_document_store_dir: str | Path,
        pdf_path: str | Path,
        loading_method: str,
    ):
        text_document_store_processor = TextDocumentStoreProcessor(
            text_document_store_dir=text_document_store_dir,
        )
        # text_document_store_processor.run(
        #     pdf_path=pdf_path,
        #     loading_method=loading_method
        # )
        txt_path = self.txt_pdf_dir / loading_method / f"{pdf_path.stem}.txt"
        text_document_store_processor.run_from_txt(
            pdf_path=pdf_path,
            loading_method=loading_method,
            txt_path=txt_path,
        )

    def _get_pdf_paths(
        self,
        pdf_dir: str | Path,
    ) -> list[Path]:
        pdf_paths = list(pdf_dir.glob('*.pdf'))
        return pdf_paths

