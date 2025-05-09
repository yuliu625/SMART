"""
文件树结构为:
- base_dir
    - original_pdf
    - image_pdf
    - document_store
        - text
            - ${loading_method}
        - image
            - ${loading_method}
    - vector_store
        - text
            - ${embedding_method--loading_method}
        - image
            - ${embedding_method--loading_method}
"""

from pathlib import Path


def get_default_dir(base_dir: str | Path):
    base_dir = Path(base_dir)
    default_dir = dict(
        base_dir=base_dir,
        original_pdf_dir = base_dir / 'original_pdf',
        base_image_pdf_dir = base_dir / 'image_pdf',
        document_store_dir = base_dir / 'document_store',
        text_document_store_dir = base_dir / 'document_store' / 'text',
        image_document_store_dir = base_dir / 'document_store' / 'image',
        vector_store_dir = base_dir / 'vector_store',
        text_vector_store_dir=base_dir / 'vector_store' / 'text',
        image_vector_store_dir=base_dir / 'vector_store' / 'image',
    )
    return default_dir

