"""

"""

from .image_document_store_processor import ImageDocumentStoreProcessor

from pathlib import Path


class ImageBatchProcessor:
    """

    """
    def __init__(
        self,
        original_pdf_dir: str,
        base_image_pdf_dir: str | Path,
        image_document_store_dir: str | Path,
    ):
        self.original_pdf_dir = Path(original_pdf_dir)
        self.base_image_pdf_dir = Path(base_image_pdf_dir)
        self.image_document_store_dir = Path(image_document_store_dir)

    def batch_process(
        self,
        loading_method: list[str],
    ):
        image_pdf_dirs = self._get_image_pdf_dirs(
            original_pdf_dir=self.original_pdf_dir,
            base_image_pdf_dir=self.base_image_pdf_dir,
        )
        for loading_method in loading_method:
            for image_pdf_dir in image_pdf_dirs:
                self.run_a_processor(
                    image_document_store_dir=self.image_document_store_dir,
                    image_pdf_dir=image_pdf_dir,
                    loading_method=loading_method,
                )

    def run_a_processor(
        self,
        image_document_store_dir: str | Path,
        image_pdf_dir: str | Path,
        loading_method: str = 'none',
    ):
        image_document_store_processor = ImageDocumentStoreProcessor(
            image_document_store_dir=image_document_store_dir,
        )
        image_document_store_processor.run(
            image_pdf_dir=image_pdf_dir,
            loading_method=loading_method,
        )

    def _get_image_pdf_dirs(
        self,
        original_pdf_dir: str | Path,
        base_image_pdf_dir: str | Path,
    ) -> list[Path]:
        pdf_paths = list(original_pdf_dir.glob('*.pdf'))
        pdf_names = [pdf_path.name for pdf_path in pdf_paths]
        image_pdf_dirs = [base_image_pdf_dir / pdf_name for pdf_name in pdf_names]
        return image_pdf_dirs

