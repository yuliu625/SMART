"""
通过docling构建的markdown数据集。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pdf_processing.convert_pdf_via_docling import (
    build_pdf_pipeline_options,
    convert_pdf_via_docling,
    batch_convert_pdf_via_docling,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def default_batch_convert_pdf_via_docling(
    pdf_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    pdf_dir = Path(pdf_dir)
    result_dir = Path(result_dir)
    pdf_path_list = list(pdf_dir.rglob('*.pdf'))
    result_markdown_paths = [
        result_dir / f"{pdf_path.stem}.md"
        for pdf_path in pdf_path_list
    ]
    # 执行转换。
    pdf_pipeline_options = build_pdf_pipeline_options(
        is_do_table_structure=True,
        is_do_ocr=False,
        images_scale=2.0,
        is_extract_images=False,
    )
    batch_convert_pdf_via_docling(
        pdf_paths=pdf_path_list,
        result_markdown_paths=result_markdown_paths,
        pipeline_options=pdf_pipeline_options,
    )


def default_incremental_batch_convert_pdf_via_docling(
    pdf_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    pdf_dir = Path(pdf_dir)
    result_dir = Path(result_dir)
    pdf_path_list = list(pdf_dir.rglob('*.pdf'))
    # HACK: 简单处理list。
    result_markdown_paths = []
    for _i in range(len(pdf_path_list)):
        result_markdown_path = result_dir / f"{pdf_path_list[_i].stem}.md"
        if not result_markdown_path.exists():
            result_markdown_paths.append(result_markdown_path)
    pdf_path_list = pdf_path_list[-len(result_markdown_paths):]
    assert len(pdf_path_list) == len(result_markdown_paths)
    assert pdf_path_list[0].stem == result_markdown_paths[0].stem
    logger.info(f"PDF to convert: {len(pdf_path_list)}")
    # 执行转换。
    pdf_pipeline_options = build_pdf_pipeline_options(
        is_do_table_structure=True,
        is_do_ocr=False,
        images_scale=2.0,
        is_extract_images=False,
    )
    batch_convert_pdf_via_docling(
        pdf_paths=pdf_path_list,
        result_markdown_paths=result_markdown_paths,
        pipeline_options=pdf_pipeline_options,
    )


def default_incremental_batch_convert_pdf_via_docling_with_images(
    pdf_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    pdf_dir = Path(pdf_dir)
    result_dir = Path(result_dir)
    pdf_path_list = list(pdf_dir.rglob('*.pdf'))
    # HACK: 简单处理list。
    result_markdown_paths = []
    for _i in range(len(pdf_path_list)):
        result_markdown_path = result_dir / f"{pdf_path_list[_i].stem}.md"
        if not result_markdown_path.exists():
            result_markdown_paths.append(result_markdown_path)
    pdf_path_list = pdf_path_list[-len(result_markdown_paths):]
    assert len(pdf_path_list) == len(result_markdown_paths)
    assert pdf_path_list[0].stem == result_markdown_paths[0].stem
    logger.info(f"PDF to convert: {len(pdf_path_list)}")
    # 执行转换。
    pdf_pipeline_options = build_pdf_pipeline_options(
        is_do_table_structure=True,
        is_do_ocr=False,
        images_scale=2.0,
        is_extract_images=True,
    )
    batch_convert_pdf_via_docling(
        pdf_paths=pdf_path_list,
        result_markdown_paths=result_markdown_paths,
        pipeline_options=pdf_pipeline_options,
    )


def main(

):
    ...


if __name__ == '__main__':
    # 默认转换方法。
    ## 无图片。
    pdf_dir_ = r"/home/liuyu/liuyu_nfs_data/pdf_dataset/raw_pdf_sample_1"
    result_dir_ = r"/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_1"
    # default_batch_conver_pdf_via_docling(
    #     pdf_dir=pdf_dir_,
    #     result_dir=result_dir_,
    # )
    default_incremental_batch_convert_pdf_via_docling(
        pdf_dir=pdf_dir_,
        result_dir=result_dir_,
    )
    ## 有图片。
    pdf_dir_ = r"/home/liuyu/liuyu_nfs_data/pdf_dataset/raw_pdf_sample_1"
    result_dir_ = r"/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/docling_2"
    default_incremental_batch_convert_pdf_via_docling_with_images(
        pdf_dir=pdf_dir_,
        result_dir=result_dir_,
    )

