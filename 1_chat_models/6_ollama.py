from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage(content="Solve the following math problems"),
    HumanMessage(content="What is 81 divided by 9?"),
]


# ---- LangChain OpenAI Chat Model Example ----

# Create a ChatOpenAI model
model = ChatOllama(model="llama3")

# Invoke the model with messages
result = model.invoke(messages)
print(f"Answer from Ollama: {result.content}")
