"""Baidu Ernie Bot LLM.

This module is to run the Baidu Ernie Bot LLM API.
"""


from .base import LLM


class BaiduErnieBot(LLM):
    """Baidu Ernie Bot LLM."""

    model: str = "models/text-bison-001"

    def __init__(self, api_key: str, **kwargs):
        """Initialize Baidu Ernie Bot LLM connection."""

    def call(self, instruction: str, value: str, suffix: str = "") -> str:
        """Call Baidu Ernie Bot LLM."""
