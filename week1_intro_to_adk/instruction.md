# Week 1 — Intro to ADK: Running Agents Locally with Ollama

> **Series:** 52 Weeks of Google Agent Development Kit  
> **Topic:** Using Ollama as a local model backend for ADK agents  
> **Source:** [adk.dev/agents/models/ollama](https://adk.dev/agents/models/ollama/)

---

## What You'll Learn

- What Google ADK is and why it matters
- How to connect ADK to a locally-running Ollama model
- How to give your agent tools (functions it can call)
- How to run the agent via `adk web` or directly in Python

---

## Prerequisites

| Requirement | Notes |
|---|---|
| Python 3.10+ | [python.org](https://python.org) |
| Ollama | [ollama.com](https://ollama.com) — install and start the server |
| A tool-capable model | See model choice section below |

---

## Step 1 — Install Dependencies

```bash
pip install google-adk litellm
```

---

## Step 2 — Pull a Tool-Capable Ollama Model

Not all Ollama models support tool/function calling. Pick one that does:

```bash
# Recommended for tool use
ollama pull mistral-small3.1

# Verify it has tool support
ollama show mistral-small3.1
```

You should see `tools` listed under **Capabilities**:

```
Capabilities
  completion
  vision
  tools        ← this is required
```

Browse all tool-capable models at: https://ollama.com/search?c=tools

---

## Step 3 — Configure the .env File

The `.env` file in this folder is automatically loaded by ADK at startup — no manual `export` needed:

```ini
OLLAMA_API_BASE=http://localhost:11434
```

> ⚠️ **Important:** Always use the `ollama_chat` provider prefix (not `ollama`) when specifying the model in ADK. Using `ollama` can cause infinite tool call loops.

---

## Step 4 — Run the Agent

### Option A — ADK Web UI (recommended for beginners)

```bash
# Run from the repo root — ADK picks up week1_intro_to_adk automatically
adk web
```

Then open http://localhost:8000 in your browser and chat with your agent.

### Option B — ADK run (terminal chat)

```bash
adk run week1_intro_to_adk
```

---

## Understanding the Code

### The Model

```python
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(model="ollama_chat/mistral-small3.1")
```

ADK uses LiteLLM as a bridge to Ollama. Always use the `ollama_chat/` prefix.

### The Agent

```python
from google.adk.agents import Agent

root_agent = Agent(
    model=model,
    name="local_assistant",
    instruction="You are a helpful local assistant...",
    tools=[get_weather, add_numbers],
)
```

- `instruction` — the system prompt that shapes your agent's behavior
- `tools` — Python functions the agent can call autonomously

### The Tools

Any regular Python function with type hints and a docstring becomes a tool:

```python
def get_weather(city: str) -> dict:
    """Returns weather for the given city."""
    ...
```

ADK automatically generates the tool schema from your function signature.

---

## Alternative: Use OpenAI Provider

If you prefer the OpenAI-compatible endpoint:

```bash
export OPENAI_API_BASE="http://localhost:11434/v1"
export OPENAI_API_KEY="anything"
```

```python
model = LiteLlm(model="openai/mistral-small3.1")
```

---

## Debugging

Add this right after your imports to see the raw requests sent to Ollama:

```python
import litellm
litellm._turn_on_debug()
```

---

## Project Structure

```
week1_intro_to_adk/
├── agent.py           # Agent definition — ADK looks for root_agent here
├── .env               # Ollama environment variables — loaded automatically
└── instruction.md     # This file
```

---

## Next Steps

- Week 2: Multi-tool agents and tool chaining
- Week 3: Sessions & memory — making your agent remember context
- Full roadmap: See [README.md](../README.md) at the repo root

---

## Resources

- ADK Ollama docs: https://adk.dev/agents/models/ollama/
- Ollama model library: https://ollama.com/search?c=tools
- ADK GitHub: https://github.com/google/adk-python
- This repo: https://github.com/singaravelan/adk-linkedin-series
