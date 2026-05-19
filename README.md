# 52 Weeks of Google Agent Development Kit (ADK)

> A weekly LinkedIn series by [Singaravelan G](https://github.com/singaravelan) exploring Google's Agent Development Kit — from local model setup to production-grade multi-agent systems.

**Source of truth:** [adk.dev](https://adk.dev)  
**Follow on LinkedIn:** Search for **Singaravelan G**

---

## How This Series Works

Each week:
- 📖 A LinkedIn post covering one ADK concept
- 💻 Working Python code in this repo
- 🔗 Links to official adk.dev documentation

---

## Series Roadmap

| Week | Topic | Folder | Status |
|------|-------|--------|--------|
| 1 | Running Agents Locally with Ollama — Intro to ADK | [week1_intro_to_adk](./week1_intro_to_adk/) | ✅ Published |
| 2 | ADK vs. Other Agent Frameworks | week2_adk_vs_frameworks | 🔜 Coming |
| 3 | Getting Started with ADK in Python | week3_getting_started_python | 🔜 Coming |
| 4 | ADK Python Project Structure — Best practices | week4_project_structure | 🔜 Coming |
| 5 | ADK Python Installation & Advanced Setup | week5_advanced_setup | 🔜 Coming |
| 6 | Coding ADK Agents with AI — AI-assisted scaffolding | week6_coding_with_ai | 🔜 Coming |
| 7 | ADK Technical Architecture — Deep dive | week7_architecture | 🔜 Coming |
| 8 | The ADK CLI — Power tools for agent developers | week8_adk_cli | 🔜 Coming |
| 9 | LLM Agents in ADK — The core building block explained | week9_llm_agents | 🔜 Coming |
| 10 | Workflow Agents — Sequential, Loop, and Parallel demystified | week10_workflow_agents | 🔜 Coming |
| 11 | Sequential Agents — Designing step-by-step agent pipelines | week11_sequential_agents | 🔜 Coming |
| 12 | Loop Agents — Iterative reasoning and when to use it | week12_loop_agents | 🔜 Coming |
| 13 | Parallel Agents — Running tasks concurrently | week13_parallel_agents | 🔜 Coming |
| 14 | Custom Agents — Going beyond built-in agent types | week14_custom_agents | 🔜 Coming |
| 15 | Multi-Agent Systems — Orchestrating teams of specialized agents | week15_multi_agent_systems | 🔜 Coming |
| 16 | Agent Routing — How ADK directs tasks to the right agent | week16_agent_routing | 🔜 Coming |
| 17 | Agent Configuration — Fine-tuning agent behavior | week17_agent_config | 🔜 Coming |
| 18 | The ADK Visual Builder — Building agents without writing code | week18_visual_builder | 🔜 Coming |
| 19 | Using Gemini with ADK — Google's flagship model in action | week19_gemini | 🔜 Coming |
| 20 | Using Claude with ADK — Cross-model flexibility in practice | week20_claude | 🔜 Coming |
| 21 | Running Local Models with ADK — Ollama and vLLM integration | [week21_local_models](./week1_intro_to_adk/) | 🔜 Coming |
| 22 | LiteLLM and ADK — Universal model routing made easy | week22_litellm | 🔜 Coming |
| 23 | Model Routing in ADK — Dynamically selecting the right model | week23_model_routing | 🔜 Coming |
| 24 | Function Tools in ADK — Building custom tools for your agents | week24_function_tools | 🔜 Coming |
| 25 | MCP Tools — Connecting agents to the Model Context Protocol ecosystem | week25_mcp_tools | 🔜 Coming |
| 26 | OpenAPI Tools — Turning any REST API into an agent capability | week26_openapi_tools | 🔜 Coming |
| 27 | How ADK Manages Context — Treating context like source code | week27_context | 🔜 Coming |
| 28 | Context Caching in ADK — Reducing latency and cost at scale | week28_context_caching | 🔜 Coming |
| 29 | Context Compression — Keeping agents fast over long sessions | week29_context_compression | 🔜 Coming |
| 30 | Sessions in ADK — Managing stateful agent conversations | week30_sessions | 🔜 Coming |
| 31 | State Management — Passing and persisting data across agent turns | week31_state_management | 🔜 Coming |
| 32 | Memory in ADK — Short-term vs. long-term memory patterns | week32_memory | 🔜 Coming |
| 33 | The ADK Agent Runtime — How agents run in production | week33_agent_runtime | 🔜 Coming |
| 34 | ADK Web Interface — Visualizing and debugging agents in the browser | week34_web_interface | 🔜 Coming |
| 35 | Deploying ADK Agents to Cloud Run | week35_cloud_run | 🔜 Coming |
| 36 | Deploying ADK Agents to GKE — Enterprise-grade Kubernetes deployments | week36_gke | 🔜 Coming |
| 37 | Ambient Agents — Agents that run in the background autonomously | week37_ambient_agents | 🔜 Coming |
| 38 | Resuming and Cancelling Agent Runs — Building reliable workflows | week38_resume_cancel | 🔜 Coming |
| 39 | Runtime Configuration — Tuning agent execution for performance and cost | week39_runtime_config | 🔜 Coming |
| 40 | Observability in ADK — Logging, Metrics, and Traces for production agents | week40_observability | 🔜 Coming |
| 41 | Evaluating ADK Agents — Going beyond vibes with structured evaluation | week41_evaluation | 🔜 Coming |
| 42 | User Simulation for Agent Testing — Automated QA for conversational agents | week42_user_simulation | 🔜 Coming |
| 43 | Custom Metrics in ADK Eval — Defining what 'good' means for your agent | week43_custom_metrics | 🔜 Coming |
| 44 | Optimizing Agents with ADK — Closing the loop from eval to improvement | week44_optimization | 🔜 Coming |
| 45 | Callbacks in ADK — Hooking into the agent lifecycle | week45_callbacks | 🔜 Coming |
| 46 | Artifacts in ADK — Handling files and binary data in agent workflows | week46_artifacts | 🔜 Coming |
| 47 | The ADK Event Loop — Understanding the heartbeat of an ADK agent | week47_event_loop | 🔜 Coming |
| 48 | ADK Plugins — Extending the framework with reusable components | week48_plugins | 🔜 Coming |
| 49 | Agent-to-Agent (A2A) Protocol — How ADK agents communicate | week49_a2a_protocol | 🔜 Coming |
| 50 | Streaming with Gemini Live API — Real-time audio, video, and images | week50_streaming | 🔜 Coming |
| 51 | ADK 2.0 — Graph-Based Workflows, Agent Teams, and What's New | week51_adk2 | 🔜 Coming |
| 52 | The Year in Review — Key ADK milestones, lessons learned, and what's next | week52_year_review | 🔜 Coming |

---

## Getting Started

```bash
# Clone this repo
git clone https://github.com/singaravelan/adk-linkedin-series.git
cd adk-linkedin-series

# Install ADK
pip install google-adk

# Jump into any week's folder and follow the instruction.md
cd week1_intro_to_adk
cat instruction.md
```

---

## Resources

- Official docs: [adk.dev](https://adk.dev)
- ADK Python: [github.com/google/adk-python](https://github.com/google/adk-python)
- ADK TypeScript: [github.com/google/adk-js](https://github.com/google/adk-js)
- Community: [adk.dev/community](https://adk.dev/community/)

---

*Built with ❤️ to help the developer community explore Google ADK one week at a time.*
