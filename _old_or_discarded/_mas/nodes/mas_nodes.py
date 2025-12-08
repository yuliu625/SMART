"""
validator要求analysis-agent进行验证的时候，中间的路由处理node。
"""

from __future__ import annotations

from mas.schemas import MASState

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:

def route_verification_request(state: MASState):
    """
    将需要验证的信息写入对应的state的字段的值中。

    能进入这个节点已经确定会进行验证。

    Args:
        state:

    Returns:

    """
    if state.current_agent_name not in ['control_analyst', 'financial_analyst', 'strategic_analyst']:
        return {'current_agent_name': 'arbiter'}

