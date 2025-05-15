"""

"""

from ..states import MASState

from typing import Literal


def condition_more_information(state: MASState) -> bool:
    """
    analyst判断是否需要更多的信息。

    Args:
        state:

    Returns:
        True: 需要更多的信息。具体的，会请求retriever从中获得更多的信息。
        False: 不需要更多的信息。已经完成分析。具体的，会请求validator进行验证。
    """
    if state == MASState.more_information:
        return True
    else:
        return False

