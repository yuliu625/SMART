"""

"""

from .text import TextBatchProcessor
from .image import PdfImageConverter, ImageBatchProcessor
from _old_or_discarded._mas.utils import get_default_dir

from pathlib import Path


class BatchProcessor:
    """

    """
    def __init__(
        self,
        base_dir: str,
        original_pdf_dir: str | Path,
        base_image_pdf_dir: str | Path,
        text_document_store_dir: str | Path,
        image_document_store_dir: str | Path,
    ):
        self.default_dir = get_default_dir(base_dir=base_dir)
        self.base_dir = self.default_dir.base_dir
        self.original_pdf_dir = Path(original_pdf_dir)
        self.base_image_pdf_dir = Path(base_image_pdf_dir)
        self.text_document_store_dir = Path(text_document_store_dir)
        self.image_document_store_dir = Path(image_document_store_dir)

    def run(
        self,
        text_loading_methods: list[str],
        image_loading_methods: list[str],
        convert_image_method: str = 'none',  # ['force', 'incremental', 'none']
    ):
        if convert_image_method == 'force':
            self.convert_pdf_to_image(
                original_pdf_dir=self.original_pdf_dir,
                base_image_pdf_dir=self.base_image_pdf_dir,
                force_overwrite=True,
            )
        elif convert_image_method == 'incremental':
            self.convert_pdf_to_image(
                original_pdf_dir=self.original_pdf_dir,
                base_image_pdf_dir=self.base_image_pdf_dir,
                force_overwrite=False,
            )
        self.process_text(
            original_pdf_dir=self.original_pdf_dir,
            text_document_store_dir=self.text_document_store_dir,
            loading_methods=text_loading_methods,
        )
        self.process_image(
            original_pdf_dir=self.original_pdf_dir,
            base_image_pdf_dir=self.base_image_pdf_dir,
            image_document_store_dir=self.image_document_store_dir,
            loading_methods=image_loading_methods,
        )

    def convert_pdf_to_image(
        self,
        original_pdf_dir: str | Path,
        base_image_pdf_dir: str | Path,
        force_overwrite: bool,
    ) -> None:
        pdf_image_converter = PdfImageConverter()
        pdf_image_converter.batch_convert_pdf_to_images(
            pdf_dir=original_pdf_dir,
            dir_to_save=base_image_pdf_dir,
            force_overwrite=force_overwrite,
        )

    def process_text(
        self,
        original_pdf_dir: str | Path,
        text_document_store_dir: str | Path,
        loading_methods: list[str],
    ) -> None:
        text_batch_processor = TextBatchProcessor(
            base_dir=self.base_dir
        )
        text_batch_processor.batch_process(loading_methods=loading_methods)

    def process_image(
        self,
        original_pdf_dir: str | Path,
        base_image_pdf_dir: str | Path,
        image_document_store_dir: str | Path,
        loading_methods: list[str],
    ) -> None:
        image_batch_processor = ImageBatchProcessor(
            original_pdf_dir=original_pdf_dir,
            base_image_pdf_dir=base_image_pdf_dir,
            image_document_store_dir=image_document_store_dir,
        )
        image_batch_processor.batch_process(loading_methods=loading_methods)

