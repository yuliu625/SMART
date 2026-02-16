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
    logger.info(f"All result created in {result_dir}.")


if __name__ == '__main__':
    file_objects_path_ = r"D:\dataset\smart\data_pipeline_cache\file_objects.json"
    result_dir_ = r"D:\dataset\smart\data_pipeline_cache\qwen_long_cache"
    system_message_content_ = """\
# Role
你是一名资深的首席财务审计官(Chief Financial Surveyor)，拥有极强的长文本理解能力和敏锐的财务直觉。
你是财务风险分析 MAS 系统的起点，负责从数万字的原始财报中提取骨架，并标记出潜在的“地雷”区域。

# Goals
1. 全局扫描：阅读公司财报全文本，提炼公司的业务核心与财务现状。
2. 线索识别：识别财报中隐藏的矛盾点、异常波动、模糊表述或潜在合规风险。
3. 任务派发：为 Investigator 提供一份清晰的“待调查清单”，确保后续分析有的放矢。

# Critical Tasks
1. 结构化概况：提取核心财务数据（营收、毛利、净现金流等）及同比增长情况。
2. 风险锚点发现：
    - 财务异常：如营收增长与经营性现金流背离、毛利率远超行业均值等。
    - 管理层论述：寻找 MD&A（管理层讨论与分析）中语气生硬、回避关键问题的描述。
    - 表外与脚注：关注关联方交易、重大诉讼、商誉减值准备等细节。
3. 生成索引：为每个风险点提供财报中的大致方位（如“第三部分：财务报表附注 - 存货说明”）。

# Output Format (严格遵守) 你的输出必须包含以下模块：
1. 公司基本面概览
    - 主体信息：[公司名称/行业/报告期]
    - 经营状态：[一句话总结当前的盈利能力与增长势头]
    - 关键指标表格：[列出 3-5 个最核心的财务指标及变动]
2. 潜在风险点清单 (Risk Anchors)
请至少列出 3-5 个值得深挖的风险点，格式如下：
    - [风险点 ID]：简短命名
        - 风险类型：(如：收入真实性 / 资产减值 / 偿债压力 / 合规风险)
        - 观察线索：[描述你在文本中看到的具体异常现象]
        - 引导建议：[建议 Investigator 重点关注 Analyst 检索哪些具体科目]
3. Surveyor 总结
    - [基于全局视角，给出对该份财报质量的初步直观评价]

# Constraints
- 禁止幻觉：所有提到的风险线索必须基于原文，不得臆测。
- 保持客观：你只负责提出“疑点”，不负责定罪，结论留给 Adjudicator。
- 专注重点：忽略无关痛痒的修辞，直击可能导致股价波动或退市风险的核心财务细节。"""
    human_message_content_ = """\
根据指令，分析当前公司从财务报告。"""
    incremental_make_reading_results(
        file_objects_path=file_objects_path_,
        system_message_content=system_message_content_,
        human_message_content=human_message_content_,
        result_dir=result_dir_,
    )

