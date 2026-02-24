"""
使用基于 qdrant 体系 pipeline 构建 vector store 。
"""

from __future__ import annotations
from loguru import logger

from rag.qdrant_vector_store_pipeline import QdrantVectorStorePipeline

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def incremental_make_qdrant_vector_store_dir_via_bge_m3(
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
            QdrantVectorStorePipeline.make_vector_store_via_native_bge_m3(
                markdown_file_path=markdown_file_path,
                headers_to_split_on=[
                    ("#", "Header 1"),
                    ("##", "Header 2"),
                    ("###", "Header 3"),
                    # ("####", "Header 4"),
                ],
                embedding_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
                embedding_model_configs=dict(batch_size=1),
                vector_store_path=result_path,
            )
            logger.success(f"Created vector store dir: {result_path}")


def incremental_make_qdrant_vector_store_dir_via_bge_m3_for_hf(
    markdown_files_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    markdown_files_dir = Path(markdown_files_dir)
    result_dir = Path(result_dir)
    markdown_files_dir.mkdir(parents=True, exist_ok=True)
    markdown_file_path_list = list(markdown_files_dir.glob('*.md'))
    # hf embedding model
    bge_m3_embedding_model = QdrantVectorStorePipeline.build_bge_m3_embedding_model(
        embedding_model_name_or_path=r"/home/liuyu/liuyu_nfs_data/model/BAAI/bge-m3",
        embedding_model_configs=dict(batch_size=1),
    )
    for markdown_file_path in markdown_file_path_list:
        # 以文件夹管理，因此没有扩展名。
        result_path = result_dir / f"{markdown_file_path.stem}"
        if not result_path.exists():
            QdrantVectorStorePipeline.batch_make_vector_store_via_native_bge_m3(
                markdown_file_path=markdown_file_path,
                headers_to_split_on=[
                    ("#", "Header 1"),
                    ("##", "Header 2"),
                    ("###", "Header 3"),
                    # ("####", "Header 4"),
                ],
                bge_m3_embedding_model=bge_m3_embedding_model,
                vector_store_path=result_path,
            )
            logger.success(f"Created vector store dir: {result_path}")


def main() -> None:
    # incremental_make_qdrant_vector_store_dir_via_bge_m3(
    #     markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
    #     result_dir=r'/home/liuyu/liuyu_nfs_data/smart_bge_m3_vector_store'
    # )
    incremental_make_qdrant_vector_store_dir_via_bge_m3_for_hf(
        markdown_files_dir=r'/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1',
        result_dir=r'/home/liuyu/liuyu_nfs_data/smart_bge_m3_vector_store'
    )


if __name__ == '__main__':
    main()

