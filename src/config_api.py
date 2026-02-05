from langchain.chat_models import init_chat_model
from LLM_Config.LLMConfig import LLMConfig as lc

def create_chat_model():
    provider = lc.PROVIDER

    if provider == "openai":
        return init_chat_model(
            model=lc.OPENAI["model"],
            model_provider="openai",
            base_url=lc.OPENAI["base_url"],
            api_key=lc.OPENAI["api_key"],
        )

    if provider == "ollama":
        return init_chat_model(
            model=lc.OLLAMA["model"],
            model_provider="ollama",
            base_url=lc.OLLAMA["base_url"],
        )

    raise ValueError(f"Unsupported LLM_PROVIDER: {provider}")

if __name__ == '__main__':

    model = create_chat_model()
    quest = "介绍一下自己"
    result = model.invoke(quest)
    print(result)