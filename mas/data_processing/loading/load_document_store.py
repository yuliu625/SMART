"""

"""

from .batch_processor import BatchProcessor

from pathlib import Path


def _get_default_dir(base_dir: str | Path):
    base_dir = Path(base_dir)
    default_dir = dict(
        original_pdf_dir = base_dir / 'original_pdf',
        base_image_pdf_dir = base_dir / 'image_pdf',
        document_store_dir = base_dir / 'document_store',
        text_document_store_dir = base_dir / 'document_store' / 'text',
        image_document_store_dir = base_dir / 'document_store' / 'image',
    )
    return default_dir


def load_document_store(
    base_dir: str | Path,
    text_loading_method: list[str],
    image_loading_method: list[str],
    convert_image_method: str,  # ['force', 'incremental', 'none']
    sub_dir_dict: dict = None,
):
    if sub_dir_dict is None:
        sub_dir_dict = _get_default_dir(base_dir)

    batch_processor = BatchProcessor(
        original_pdf_dir=sub_dir_dict['original_pdf_dir'],
        base_image_pdf_dir=sub_dir_dict['base_image_pdf_dir'],
        text_document_store_dir=sub_dir_dict['text_document_store_dir'],
        image_document_store_dir=sub_dir_dict['image_document_store_dir'],
    )
    batch_processor.run(
        text_loading_methods=text_loading_method,
        image_loading_methods=image_loading_method,
        convert_image_method=convert_image_method,
    )

