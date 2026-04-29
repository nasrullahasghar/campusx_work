# Chat Models using OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = load_dotenv(model='gpt-4', temperature=1.5, max_completion_tokens=10)

result = model.invoke("What is the Capital of Pakistan?")
print(result.content)