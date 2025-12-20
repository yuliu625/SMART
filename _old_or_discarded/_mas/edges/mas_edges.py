"""

"""

from __future__ import annotations

from _old_or_discarded._mas.schemas import MASState

from typing import TYPE_CHECKING, Literal
# if TYPE_CHECKING:


def is_need_verification(state: MASState) -> bool:
    """
    是否进行验证的edge。

    Args:
        state:

    Returns:

    """
    if state.remaining_validation_rounds == 0:
        # 如果已经到达最大验证次数，不再进行验证。
        return False
    if state.is_need_verification:
        # 如果需要验证，进行验证。
        return True
    else:
        return False


def call_analysis_agents(
    state: MASState,
) -> Literal['arbiter', 'control_analyst', 'financial_analyst', 'strategic_analyst']:
    """
    验证选择路由。

    Args:
        state:

    Returns:
        arbiter, 已经收集到足够的信息，可以进行仲裁。
        analyst, 请求某个analyst进行进一步分析。
    """
    if state.current_agent_name in ['control_analyst', 'financial_analyst', 'strategic_analyst']:
        return state.current_agent_name
    else:
        return 'arbiter'

