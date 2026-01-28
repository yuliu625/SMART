"""
收集各种条件下的运行结果。

包含直接返回收集结果，以及直接完成序列化。
"""

from __future__ import annotations
from loguru import logger

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def main():
    print(ResultCollector.collect_decision_results(target_dir=r"D:\dataset\smart\tests"))


if __name__ == '__main__':
    st_companies_path_ = r"D:\dataset\smart\original_data\csmar\st_companies_in_2024.xlsx"
    matching_sample_path_ = r"D:\dataset\smart\original_data\csmar\matching_sample_1_in_2024.xlsx"
    main()

