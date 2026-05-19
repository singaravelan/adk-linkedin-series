from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

root_agent = Agent(
    model=LiteLlm(model="ollama_chat/mistral-small3.1"),
    name="local_assistant",
    description="A local AI assistant powered by Ollama.",
    instruction="You are a helpful assistant running entirely on the user's machine via Ollama. Be concise and friendly.",
)
