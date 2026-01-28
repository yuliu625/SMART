"""
结果收集工具。

该方法直接和mas中的schema和IOMethods对应。
"""

from __future__ import annotations
from loguru import logger

from pathlib import Path
import json
import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class ResultCollector:
    """
    自动结果收集器。

    因为在原始构建的MAS中，最终要求输出结果的字段和结构都是一致的。
    """
    @staticmethod
    def collect_decision_results(
        target_dir: str | Path,
    ) -> list[dict]:
        target_dir = Path(target_dir)
        result_json_path_list = list(target_dir.glob('*.json'))
        all_results = []
        for result_json_path in result_json_path_list:
            content = result_json_path.read_text(encoding='utf-8')
            data = json.loads(content)
            result_dict = ResultCollector.extract_visualization_results(
                result_dict=data,
            )
            all_results.append(
                dict(
                    Stkcd=result_json_path.stem,
                    **result_dict,
                )
            )
        return all_results

    @staticmethod
    def extract_decision(
        result_dict: dict,
    ) -> dict:
        return result_dict['final_decision']

    @staticmethod
    def extract_visualization_results(
        result_dict: dict,
    ) -> dict:
        result = dict(
            has_risk=result_dict['final_decision']['has_risk'],
            confidence=result_dict['final_decision']['confidence'],
        )
        return result

