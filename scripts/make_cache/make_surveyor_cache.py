"""
构建 MAS 运行可直接使用的 cache 。
"""

from __future__ import annotations
from loguru import logger

from data_processing.cache.openai_completion_parser import (
    OpenAICompletionParser,
)
from data_processing.cache.openai_file_id_and_name_mapping import (
    OpenAIFileIdAndNameMappingMethods,
)

from pathlib import Path
import json

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def make_surveyor_human_message_content_cache(
    file_objects_path: str | Path,
    target_dir: str | Path,
    result_dir: str | Path,
) -> None:
    # process path
    target_dir = Path(target_dir)
    result_dir = Path(result_dir)
    result_dir.mkdir(parents=True, exist_ok=True)
    # load file objects
    file_objects = json.loads(file_objects_path)
    file_id_to_file_name_mapping = OpenAIFileIdAndNameMappingMethods.collect_file_id_to_name_mapping(
        file_objects=file_objects,
    )
    for file_id, file_name in file_id_to_file_name_mapping.items():
        target_file_path = target_dir / f"{file_name}.json"
        result_file_path = result_dir / Path(file_name).with_suffix('.txt')
        completion = json.loads(
            target_file_path.read_text(encoding='utf-8')
        )
        content = OpenAICompletionParser.extract_content(
            completion=completion,
        )
        result_file_path.write_text(
            content,
            encoding='utf-8',
        )
        logger.success(f"Saved {file_name} to {target_file_path}")


if __name__ == '__main__':
    file_objects_path_ = r"D:\dataset\smart\data_pipeline_cache\file_objects.json"
    target_dir_ = r"D:\dataset\smart\data_pipeline_cache\qwen_long_cache"
    result_dir_ = r"D:\dataset\smart\data_pipeline_cache\surveyor_cache"
    make_surveyor_human_message_content_cache(
        file_objects_path=file_objects_path_,
        target_dir=target_dir_,
        result_dir=result_dir_,
    )

