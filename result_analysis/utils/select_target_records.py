"""
选择目标记录的方法。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


def select_target_records_by_id(
    original_df: pd.DataFrame,
    target_ids: pd.Series,
    target_id_name: str,
    target_field_name: str,
) -> pd.DataFrame:
    result_df = target_ids.to_frame().merge(
        original_df[[target_id_name, target_field_name]],
        left_on=target_id_name,
        right_on=target_id_name,
        how="inner",
    )
    return result_df

