"""

"""

from .text import TextBatchIndexer
from .image import ImageBatchIndexer
from mas.utils import get_default_dir


from pathlib import Path


def build_image_vector_store(
    base_dir: str | Path,
    image_embedding_methods: list[str],
    image_loading_methods: list[str],
    sub_dir_dict: dict = None,
):
    if sub_dir_dict is None:
        sub_dir_dict = get_default_dir(base_dir)

    image_batch_indexer = ImageBatchIndexer(
        original_pdf_dir=sub_dir_dict['original_pdf_dir'],
        base_image_pdf_dir=sub_dir_dict['base_image_pdf_dir'],
        image_vector_store_dir=sub_dir_dict['image_vector_store_dir'],
    )
    image_batch_indexer.batch_process(
        loading_methods=image_loading_methods,
        embedding_methods=image_embedding_methods,
    )


def build_text_vector_store(
    base_dir: str | Path,
    text_embedding_methods: list[str],
    text_loading_methods: list[str],
    sub_dir_dict: dict = None,
):
    if sub_dir_dict is None:
        sub_dir_dict = get_default_dir(base_dir)

    text_batch_indexer = TextBatchIndexer(
        base_dir=base_dir
    )
    text_batch_indexer.batch_process(
        loading_methods=text_loading_methods,
        embedding_methods=text_embedding_methods,
    )

