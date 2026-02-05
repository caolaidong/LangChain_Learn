import os
from dotenv import load_dotenv
from pathlib import Path

# 项目根目录（假设 src 是源码根）
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

class LLMConfig:
    PROVIDER = os.getenv("LLM_PROVIDER")

    OPENAI = {
        "api_key": os.getenv("OPENAI_API_KEY"),
        "base_url": os.getenv("OPENAI_BASE_URL"),
        "model": os.getenv("OPENAI_MODEL"),
    }

    OLLAMA = {
        "base_url": os.getenv("OLLAMA_BASE_URL"),
        "model": os.getenv("OLLAMA_MODEL"),
    }
if __name__ == '__main__':
    print("DEBUG LLM_PROVIDER raw:", os.getenv("LLM_PROVIDER"))
    print("DEBUG OPENAI_API_KEY raw:", os.getenv("OPENAI_API_KEY"))
    print("DEBUG ENV LOADED")

