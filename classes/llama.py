from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser

OLLAMA_BASE_URL ="http://localhost:11434"

class LlamaModel:

    def __init__(self, model: str) -> None:
        self.llm = Ollama(model=model, base_url=OLLAMA_BASE_URL)
    def generate_text(self, prompt: str) -> str:
       text = self.llm.invoke(prompt)
       return text
