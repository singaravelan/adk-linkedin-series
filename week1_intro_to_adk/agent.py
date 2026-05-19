"""
Week 1 — Intro to ADK: Running Agents Locally with Ollama

Run from the parent directory with:
    adk web
"""

import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


# ---------------------------------------------------------------------------
# Tools
# ---------------------------------------------------------------------------

def get_weather(city: str) -> dict:
    """Returns a mock weather report for the given city.

    Args:
        city: The name of the city to get weather for.

    Returns:
        A dict with temperature_celsius and condition.
    """
    conditions = ["Sunny", "Cloudy", "Rainy", "Windy", "Partly Cloudy"]
    return {
        "city": city,
        "temperature_celsius": random.randint(15, 38),
        "condition": random.choice(conditions),
    }


def add_numbers(a: float, b: float) -> dict:
    """Adds two numbers and returns the result.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        A dict with the result.
    """
    return {"result": a + b}


# ---------------------------------------------------------------------------
# Agent
# ---------------------------------------------------------------------------
# ADK looks for `root_agent` in this file automatically.
# Use ollama_chat/<model> — never plain ollama — to avoid tool call loops.
# OLLAMA_API_BASE is loaded from .env by ADK at startup.

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    name="local_assistant",
    description="A local AI assistant powered by Ollama that can check weather and add numbers.",
    instruction="""
    You are a helpful assistant running entirely on the user's machine via Ollama.
    Use the available tools when the user asks for weather or calculations.
    For everything else, answer from your own knowledge.
    Always be concise and friendly.
    """,
    tools=[get_weather, add_numbers],
)
