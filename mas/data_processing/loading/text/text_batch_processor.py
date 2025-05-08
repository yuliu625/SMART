"""

"""


from .text_document_store_processor import TextDocumentStoreProcessor

from pathlib import Path


class TextBatchProcessor:
    """

    """
    def __init__(
        self,
        original_pdf_dir: str,
        text_document_store_dir: str | Path,
    ):
        self.original_pdf_dir = Path(original_pdf_dir)
        self.text_document_store_dir = Path(text_document_store_dir)

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
        text_document_store_processor.run(
            pdf_path=pdf_path,
            loading_method=loading_method
        )

    def _get_pdf_paths(
        self,
        pdf_dir: str | Path,
    ) -> list[Path]:
        pdf_paths = list(pdf_dir.glob('*.pdf'))
        return pdf_paths

