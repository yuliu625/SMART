"""
测试Analyst。
"""

from __future__ import annotations
import pytest
from loguru import logger

from mas.agent_nodes.analysis_agents.analyst import Analyst
from mas.schemas.final_mas_state import FinalMASState
from mas.schemas.structured_output_format import AnalystRequest
from mas.prompts.prompt_template_loader import PromptTemplateLoader

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from pathlib import Path

from typing import TYPE_CHECKING, cast
# if TYPE_CHECKING:


def make_test_analyst() -> Analyst:
    analyst = Analyst(
        main_llm=ChatOllama(
            model='qwen2.5:1.5b',
            temperature=0.7,
        ),
        main_llm_system_message=cast(
            SystemMessage,
            PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                system_message_prompt_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_main_llm_system_prompt_template.j2",
            ).format()
        ),
        formatter_llm=ChatOllama(
            model='qwen2.5:1.5b',
            temperature=0.7,
        ),
        schema_pydantic_base_model=AnalystRequest,
        formatter_llm_system_message=cast(
            SystemMessage,
            PromptTemplateLoader.load_system_message_prompt_template_from_j2(
                system_message_prompt_template_path=r"D:\document\code\paper\SMART\mas\prompts\final_mas\analyst_formatter_llm_system_prompt_template.j2",
            ).format()
        ),
    )
    return analyst


def make_test_final_mas_state() -> FinalMASState:
    state = FinalMASState(
        original_pdf_text=Path(
            r"D:\dataset\smart\tests\docling_1\000004.md"
        ).read_text(encoding='utf-8'),
        decision_shared_messages=[
            HumanMessage(
                content='<!--surveyor-start-->\n这份年报的内容涵盖了公司的财务状况、经营成果、现金流量等方面。以下是对报告内容的详细分析：\n\n### 财务概况与业绩表现\n\n#### 收入与成本结构\n- **收入**：公司本期营业收入为941,802.00元，其中租赁收入为941,802.00元。\n- **成本**：相关费用包括营业成本19,463.16元。\n\n#### 投资收益与非经常性损益\n- **权益法核算的长期股权投资收益**：本期产生投资收益-246,350.21元，主要来自被投资单位公允价值变动。\n- **处置长期股权投资产生的投资收益**：本期净损失为-423,619.09元。\n- **交易性金融资产在持有期间的投资收益**：本期产生投资收益211,817.70元，主要来源于持有的金融资产的公允价值变动。\n\n### 损益分析\n\n#### 净利润与每股收益\n- **净利润**：归属于普通股股东的净利润为-194,356.99元。\n- **扣除非经常性损益后的净利润**：扣除非经常性损益后，归属于普通股股东的净利润为-211,801.39元。\n\n#### 损益构成\n- **营业利润**：营业利润为-436,755.75元。\n- **利润总额**：利润总额为-563,012.26元。\n- **净利润**：净利润为-730,234.70元。\n\n#### 每股收益\n- 基本每股收益（元/股）：为-0.9936元。\n- 稀释每股收益（元/股）：同样为-0.9936元。\n\n### 净资产收益率与每股收益\n\n- **加权平均净资产收益率**：加权平均净资产收益率为-101.33%。\n- **基本每股收益**：每股收益为-0.9936元。\n- **稀释每股收益**：同样为-0.9936元。\n\n### 非经常性损益与报告期利润\n\n#### 报告期利润\n- **净利润**：归属于普通股股东的净利润为-194,356.99元，扣除非经常性损益后为-211,801.39元。\n\n### 期末情况\n\n- **期末净资产收益率**：加权平均净资产收益率为-101.33%。\n- **期末每股收益**：基本每股收益和稀释每股收益均为-0.9936元。\n\n### 其他补充信息\n\n#### 报告期内合同类型\n- 市场或客户类型：合同类型中没有列出具体内容，需要进一步查阅相关财务报表。\n\n#### 重要支付条款\n- **公司承诺转让商品的性质**：合同类型中没有详细列示。\n- **交易性金融资产在持有期间的投资收益**：交易性金融资产的公允价值变动产生的投资收益为211,817.70元，这可能涉及具体的金融资产类型和交易策略。\n\n### 境内外会计准则下会计数据差异\n\n#### 净利润与净资产\n- **净利润**：境外会计准则下，公司净利润为负数。\n- **净资产**：净资产也呈现亏损状态。\n\n### 非经常性损益与报告期利润的比较\n- **非经常性损益**：报告期内没有提及其他额外收益或费用，主要聚焦于常规经营业务和会计准则差异。\n\n#### 损益构成分析\n- **营业利润、利润总额及净利润**：均呈现亏损状态，这可能是由于公司日常运营成本较高或者投资损失导致。\n\n### 后续展望与风险提示\n\n年报最后部分提到，公司在报告期没有重大合同变更或交易价格调整。未来的发展需要关注宏观经济环境对行业的影响以及公司自身管理能力的提升。\n\n这份年报提供了公司的财务表现、利润结构及损益情况，但需要注意的是，具体的业务细节和会计政策可能不完全反映在公开的信息中，需要结合其他内部资料进行进一步分析。\n<!--surveyor-end-->',
                additional_kwargs={},
                response_metadata={},
            ),
            AIMessage(
                content='<!--investigator-start-->\n### 任务下达\n\n根据Surveyor提供的风险线索，以下是详细的风险点：\n\n1. **收入与成本结构**：本期营业收入为941,802.00元，相关费用包括营业成本19,463.16元。\n2. **投资收益与非经常性损益**：权益法核算的长期股权投资收益为-246,350.21元，主要来自被投资单位公允价值变动；处置长期股权投资产生的投资收益为-423,619.09元；交易性金融资产在持有期间的投资收益为211,817.70元。\n3. **损益分析**：营业利润为-436,755.75元，利润总额为-563,012.26元，净利润为-730,234.70元。每股收益分别为基本每股收益（元/股）和稀释每股收益（元/股），均为-0.9936元。\n4. **期末情况**：加权平均净资产收益率为-101.33%，期末净资产收益率同样为-101.33%；基本每股收益、稀释每股收益均为-0.9936元。报告期内合同类型和重要支付条款未列示，但交易性金融资产在持有期间的投资收益可能涉及具体的金融资产类型。\n5. **境内与境外会计准则下差异**：净利润为负数，净资产也呈现亏损状态；非经常性损益主要聚焦于常规经营业务和会计准则差异。\n\n### 循环审查\n\n- 从收入、成本结构到财务报表的各个部分，需要确保分析师能够提供详细的解释并验证数据的一致性和合理性。\n- **数据对比**：对于报告中的重要数字，如净利润、每股收益等，建议要求分析师进行前后期对比以及行业平均值的比较。这将有助于确认这些数值是否符合公司的正常运营模式和市场表现。\n\n### 终止条件\n\n若证据不足或逻辑不通，需继续追问以找到更有力的证据。\n\n### 提交报告\n\n最终的调查报告将包括以上所有分析结果，并附上详细的数据对比和会计准则下合理的解释。\n\n---\n\n**[ACTION: ANALYZE] -> {针对的具体问题和检索建议}**\n\n请提供关于收入、成本结构以及投资收益与非经常性损益的相关数据，以进一步验证这些信息的真实性。\n<!--investigator-end-->',
                additional_kwargs={},
                response_metadata={},
            )
        ],
        current_message="根据提供的风险点，请提供相关财务数据的详细解释，包括但不限于营业收入、营业成本、权益法核算的长期股权投资收益、交易性金融资产在持有期间的投资收益等。这将有助于我们验证这些信息的真实性，并确认其与公司的正常运营模式和市场表现相符。",
        remaining_validation_rounds=9,
        current_agent_name='analyst',
        last_agent_name='investigator',
    )
    return state


class TestAnalyst:
    @pytest.mark.parametrize(
        "analyst, state", [
        (make_test_analyst(),
         make_test_final_mas_state()),
    ])
    @pytest.mark.asyncio
    async def test_analyst_as_node_in_final_mas(
        self,
        analyst: Analyst,
        state: FinalMASState,
    ):
        logger.trace(f"\nTest State: \n{state}")
        result = await analyst.process_state(
            state=state,
            config=None,
        )
        logger.info(f"\nAnalyst Result: \n{result}")

