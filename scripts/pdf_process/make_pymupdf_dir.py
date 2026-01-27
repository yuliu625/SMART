"""
通过pymupdf构建的markdown数据集。

以下方法暂时未构建增量式处理机制，一般仅基于规则的CPU的任务不会出错，也不会花很多时间。
"""

from __future__ import annotations
from loguru import logger

from data_processing.pdf_processing.convert_pdf_via_pymupdf4llm import (
    convert_pdf_via_pymupdf4llm,
    convert_pdf_via_pymupdf4llm_with_images,
)

from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def batch_convert_pdf_via_pymupdf4llm(
    pdf_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    # 批量处理。
    pdf_dir = Path(pdf_dir)
    # 以所有的pdf文件为目标。
    ## HARDCODED: 默认方法是基于路径自动处理，无关指定目标文件。
    pdf_path_list = list(pdf_dir.glob('*.pdf'))
    for _pdf_path in pdf_path_list:
        # 命名方式: 同stem，仅修改文件后缀。
        _result_markdown_path = result_dir / f"{_pdf_path.stem}.md"
        convert_pdf_via_pymupdf4llm(
            pdf_path=_pdf_path,
            result_markdown_path=_result_markdown_path,
        )
    logger.success(f"Convert {pdf_dir} to {result_dir}.")


def batch_convert_pdf_via_pymupdf4llm_with_images(
    pdf_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 命名规则: 同级文件夹下，新建同名文件夹保存images。
    # 路径处理。
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    # 批量处理。
    pdf_dir = Path(pdf_dir)
    # 以所有的pdf文件为目标。
    ## HARDCODED: 默认方法是基于路径自动处理，无关指定目标文件。
    pdf_path_list = list(pdf_dir.glob('*.pdf'))
    for _pdf_path in pdf_path_list:
        # 命名方式: 同stem，仅修改文件后缀。
        _result_markdown_path = result_dir / f"{_pdf_path.stem}.md"
        _result_image_dir = result_dir / f"{_pdf_path.stem}"
        convert_pdf_via_pymupdf4llm_with_images(
            pdf_path=_pdf_path,
            result_markdown_path=_result_markdown_path,
            is_need_image=True,
            result_image_dir=_result_image_dir,
        )
    logger.success(f"Convert {pdf_dir} to {result_dir}.")


def main(

) -> None:
    ...


if __name__ == '__main__':
    # 最基础的转换。
    ## 无图片。
    batch_convert_pdf_via_pymupdf4llm(
        pdf_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/raw_pdf_sample_1",
        result_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_1",
    )
    ## 有图片。
    batch_convert_pdf_via_pymupdf4llm_with_images(
        pdf_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/raw_pdf_sample_1",
        result_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/pymupdf_2",
    )

