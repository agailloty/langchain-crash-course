from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

# Setup environment variables and messages
load_dotenv()

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]

# Create a Anthropic model
# Anthropic models: https://docs.anthropic.com/en/docs/models-overview
model = ChatAnthropic(model="claude-3-opus-20240229")

result = model.invoke(messages)
print(f"Answer from Anthropic: {result.content}")