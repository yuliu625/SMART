"""
validator要求analysis-agent进行验证的时候，中间的路由处理node。
"""


from ..states import MASState

from typing import Literal


def route_verification_request(state: MASState):
    """
    将需要验证的信息写入对应的state的字段的值中。

    能进入这个节点已经确定会进行验证。

    Args:
        state:

    Returns:

    """
    verification_requests = state.verification_requests
    # return state

