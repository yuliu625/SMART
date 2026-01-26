"""
通过DeepSeek-OCR转换pdf为markdown。
"""

from __future__ import annotations
# from loguru import logger

from deepseek_ocr import ModelManager, OCRProcessor
from pathlib import Path

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def convert_pdf_via_deepseek_ocr(
    pdf_path: str | Path,
    output_path: str | Path,
) -> None:
    # 该方法下的结构化构造。
    model_manager = ModelManager(
        model_name='deepseek-ocr',
    )
    model_manager.load_model()
    # 处理方法设置。
    processor = OCRProcessor(
        model_manager=model_manager,
        output_dir=None,  # 不需要图片的情况下，通过save_result方法指定保存路径。
        extract_images=False,  # 不提取图片。
        include_metadata=False,  # 不添加该工具的默认信息。
        # HARDCODED
        dpi=200,
        workers=64,
        analyze_figures=True,
    )
    # 执行处理。
    result = processor.process_file(
        file_path=Path(pdf_path),
    )
    # print(result.output_text)
    # 保存结果。
    ## 仅文本的情况下，指定路径，覆盖工具默认安排方法。
    processor.save_result(
        result=result,
        output_path=output_path,
    )
    # 该方法下的结构化析构。
    model_manager.unload_model()


def convert_pdf_via_deepseek_ocr_with_images(
    pdf_path: str | Path,
    output_dir: str | Path,
) -> None:
    # 该方法下的结构化构造。
    model_manager = ModelManager(
        model_name='deepseek-ocr',
    )
    model_manager.load_model()
    # 处理方法设置。
    processor = OCRProcessor(
        model_manager=model_manager,
        output_dir=Path(output_dir),  # 需要图片的条件下，由该工具的方法默认处理。后续再自行处理路径。
        extract_images=True,  # 需要图片
        include_metadata=False,  # 不添加该工具的默认信息。
        # HARDCODED
        dpi=200,
        workers=64,
        analyze_figures=True,
    )
    # 执行处理。
    result = processor.process_file(
        file_path=Path(pdf_path),
    )
    # print(result.output_text)
    # 保存结果。
    ## 执行提取图片的情况下，不主动指定保存路径。
    processor.save_result(
        result=result,
        # output_path=output_path,
    )
    # 该方法下的结构化析构。
    model_manager.unload_model()

