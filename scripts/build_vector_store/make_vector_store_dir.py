"""
预构建vector_store进行缓存。
"""

from __future__ import annotations
from loguru import logger

from rag.vector_store_pipeline import ChromaVectorStorePipeline

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def incremental_make_vector_store_dir_via_nomic(
    markdown_files_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    markdown_files_dir = Path(markdown_files_dir)
    result_dir = Path(result_dir)
    markdown_files_dir.mkdir(parents=True, exist_ok=True)
    markdown_file_path_list = list(markdown_files_dir.glob('*.md'))
    for markdown_file_path in markdown_file_path_list:
        # 以文件夹管理，因此没有扩展名。
        result_path = result_dir / f"{markdown_file_path.stem}"
        if not result_path.exists():
            ChromaVectorStorePipeline.make_vector_store_via_ollama(
                markdown_file_path=markdown_file_path,
                headers_to_split_on=[
                    ("#", "Header 1"),
                    ("##", "Header 2"),
                    ("###", "Header 3"),
                    ("####", "Header 4"),
                ],
                ollama_embedding_model_name=r'nomic-embed-text:v1.5',
                ollama_embedding_model_context_length=8192,
                vector_store_path=result_path,
            )


def main() -> None:
    # markdown1
    ## pymupdf1
    incremental_make_vector_store_dir_via_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/pymupdf_1',
    )
    ## pymupdf2
    incremental_make_vector_store_dir_via_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/pymupdf_2',
    )
    ## docling1
    incremental_make_vector_store_dir_via_nomic(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_vector_store/nomic/markdown_1/docling_1',
    )


if __name__ == '__main__':
    main()

