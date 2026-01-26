"""
通过deepseek-ocr构建的markdown数据集。
"""

from __future__ import annotations
# from loguru import logger

from data_processing.pdf_processing.convert_pdf_via_deepseek_ocr import (
    convert_pdf_via_deepseek_ocr,
    convert_pdf_via_deepseek_ocr_with_images,
)

from pathlib import Path
import time

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def default_incremental_batch_convert_pdf_via_deepseek_ocr(
    pdf_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    pdf_dir = Path(pdf_dir)
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    # 以所有的pdf文件为目标。
    ## HARDCODED: 默认方法是基于路径自动处理，无关指定目标文件。
    pdf_path_list = list(pdf_dir.glob('*.pdf'))
    for pdf_path in pdf_path_list:
        result_markdown_path = result_dir / f'{pdf_path.stem}.md'
        if not result_markdown_path.exists():
            convert_pdf_via_deepseek_ocr(
                pdf_path=pdf_path,
                output_path=result_markdown_path,
            )
            # 我并不知道这个工具是否正常运行的情况。间隔1s是最简单的做法。
            time.sleep(1)


def default_incremental_batch_convert_pdf_via_deepseek_ocr_with_images(
    pdf_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # 路径处理。
    pdf_dir = Path(pdf_dir)
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    # 以所有的pdf文件为目标。
    ## HARDCODED: 默认方法是基于路径自动处理，无关指定目标文件。
    pdf_path_list = list(pdf_dir.glob('*.pdf'))
    for pdf_path in pdf_path_list:
        result_with_images_dir = result_dir / f'{pdf_path.stem}'
        if not result_with_images_dir.exists():
            convert_pdf_via_deepseek_ocr_with_images(
                pdf_path=pdf_path,
                output_dir=result_with_images_dir,
            )
            # 我并不知道这个工具是否正常运行的情况。间隔1s是最简单的做法。
            time.sleep(1)


def main(

) -> None:
    ...


if __name__ == '__main__':
    # 默认转换方法。
    ## 无图片。
    default_incremental_batch_convert_pdf_via_deepseek_ocr(
        pdf_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/raw_pdf_sample_1",
        result_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_1",
    )
    ## 有图片。
    default_incremental_batch_convert_pdf_via_deepseek_ocr_with_images(
        pdf_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/raw_pdf_sample_1",
        result_dir=r"/home/liuyu/liuyu_nfs_data/pdf_dataset/markdown_1/vlm_2",
    )

