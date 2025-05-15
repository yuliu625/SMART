"""

"""

from ..states import MASState

from typing import Literal


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


def call_analysis_agents(state: MASState) -> Literal['arbiter', 'analyst']:
    """
    验证选择路由。

    Args:
        state:

    Returns:
        arbiter, 已经收集到足够的信息，可以进行仲裁。
        analyst, 请求某个analyst进行进一步分析。
    """
    request_agents = list(state.verification_requests.keys())
    if len(request_agents) == 0:
        request_agents = ['arbiter']
    return request_agents

