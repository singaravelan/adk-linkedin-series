# Week 1 — Intro to ADK: Running Agents Locally with Ollama

> **Series:** 52 Weeks of Google Agent Development Kit  
> **Topic:** Using Ollama as a local model backend for ADK agents  
> **Source:** [adk.dev/agents/models/ollama](https://adk.dev/agents/models/ollama/)

---

## What You'll Learn

- What Google ADK is and why it matters
- How to connect ADK to a locally-running Ollama model
- How to run a minimal agent via `adk web`

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

## Step 2 — Pull an Ollama Model

```bash
ollama pull mistral-small3.1
```

Browse all available models at: https://ollama.com/search

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

```python
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    name="local_assistant",
    description="A local AI assistant powered by Ollama.",
    instruction="You are a helpful assistant running entirely on the user's machine via Ollama. Be concise and friendly.",
)
```

- `model` — uses LiteLLM as a bridge to Ollama; always use the `ollama_chat/` prefix
- `instruction` — the system prompt that shapes your agent's behavior
- ADK looks for `root_agent` in `agent.py` automatically

---

## Project Structure

```
week1_intro_to_adk/
├── agent.py           # Minimal root_agent definition
├── .env               # Ollama environment variables — loaded automatically
├── .env.example       # Example env config to copy
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
