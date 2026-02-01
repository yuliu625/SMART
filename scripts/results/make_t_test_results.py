"""
对数据集结果执行t-test。
"""

from __future__ import annotations
from loguru import logger

import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency

from typing import TYPE_CHECKING
# if TYPE_CHECKING:
