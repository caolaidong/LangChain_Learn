import openai
import langchain
import sys
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="deepseek-r1:8b",
    model_provider="ollama",
    base_url="http://localhost:11434",

)

quest = "介绍一下自己"
result = model.invoke(quest)
print(result)

