"""
测试 gateway 下的响应。
"""

from __future__ import annotations
import pytest
from loguru import logger

from openai import OpenAI

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class TestInferenceServer:
    def test_surveyor(
        self,
    ):
        client = OpenAI(
            base_url='http://127.0.0.1:4000',
            api_key='none',
        )
        response = client.chat.completions.create(
            model="surveyor-llm",
            messages=[{"role": "user", "content": "What is your model id?"}]
        )
        logger.info(f"\nSurveyor Response: \n{response}")

    def test_investigator(
        self,
    ):
        client = OpenAI(
            base_url='http://127.0.0.1:4000',
            api_key='none',
        )
        response = client.chat.completions.create(
            model="investigator-llm",
            messages=[{"role": "user", "content": "What is your model id?"}]
        )
        logger.info(f"\nInvestigator Response: \n{response}")

    def test_adjudicator(
        self,
    ):
        client = OpenAI(
            base_url='http://127.0.0.1:4000',
            api_key='none',
        )
        response = client.chat.completions.create(
            model="adjudicator-llm",
            messages=[{"role": "user", "content": "What is your model id?"}]
        )
        logger.info(f"\nAdjudicator Response: \n{response}")

    def test_analyst(
        self,
    ):
        client = OpenAI(
            base_url='http://127.0.0.1:4000',
            api_key='none',
        )
        response = client.chat.completions.create(
            model="analyst-llm",
            messages=[{"role": "user", "content": "What is your model id?"}]
        )
        logger.info(f"\nAnalyst Response: \n{response}")

    def test_formatter(
        self,
    ):
        client = OpenAI(
            base_url='http://127.0.0.1:4000',
            api_key='none',
        )
        response = client.chat.completions.create(
            model="formatter-llm",
            messages=[{"role": "user", "content": "What is your model id?"}]
        )
        logger.info(f"\nFormatter Response: \n{response}")

