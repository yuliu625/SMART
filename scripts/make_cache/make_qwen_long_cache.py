"""
构建基于 qwen-long 的 cache 。
"""

from __future__ import annotations
from loguru import logger

from data_processing.cache.dashscope_reader import (
    QwenLongReader,
)
from data_processing.cache.openai_file_id_and_name_mapping import (
    OpenAIFileIdAndNameMappingMethods,
)

from pathlib import Path
import json

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def incremental_make_reading_results(
    file_objects_path: str | Path,
    system_message_content: str,
    human_message_content: str,
    result_dir: str,
) -> None:
    # process path
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    # load file objects
    file_objects = json.loads(file_objects_path)
    file_ids = OpenAIFileIdAndNameMappingMethods.collect_all_file_id(
        file_objects=file_objects,
    )
    # incremental read files
    for file_id in file_ids:
        result_path = result_dir / f"{file_id}.json"
        if result_path.exists():
            logger.info(f"Result {result_path} exists.")
            continue
        else:  # new file
            QwenLongReader.read_file_and_save_result(
                file_id=file_id,
                system_message_content=system_message_content,
                human_message_content=human_message_content,
                result_path=result_path,
            )
            logger.success(f"Result {result_path} created.")
    logger.info(f"All result created in {result_dir}")


if __name__ == '__main__':
    file_objects_path_ = r"D:\dataset\smart\data_pipeline_cache\file_objects.json"
    result_dir_ = r"D:\dataset\smart\data_pipeline_cache\qwen_long_cache"
    system_message_content_ = r"""
    """
    human_message_content_ = r"""
    """
    incremental_make_reading_results(
        file_objects_path=file_objects_path_,
        system_message_content=system_message_content_,
        human_message_content=human_message_content_,
        result_dir=result_dir_,
    )

