"""

"""

from .batch_processor import BatchProcessor
from _old_or_discarded._mas.utils import get_default_dir

from pathlib import Path

from typing import Literal


def build_document_store(
    base_dir: str | Path,
    text_loading_methods: list[str],
    image_loading_methods: list[str],
    convert_image_method: Literal['force', 'incremental', 'none'] = 'incremental',  # ['force', 'incremental', 'none']
    sub_dir_dict: dict = None,
):
    if sub_dir_dict is None:
        sub_dir_dict = get_default_dir(base_dir)

    batch_processor = BatchProcessor(
        base_dir=base_dir,
        original_pdf_dir=sub_dir_dict.original_pdf_dir,
        base_image_pdf_dir=sub_dir_dict.base_image_pdf_dir,
        text_document_store_dir=sub_dir_dict.text_document_store_dir,
        image_document_store_dir=sub_dir_dict.image_document_store_dir,
    )
    batch_processor.run(
        text_loading_methods=text_loading_methods,
        image_loading_methods=image_loading_methods,
        convert_image_method=convert_image_method,
    )

