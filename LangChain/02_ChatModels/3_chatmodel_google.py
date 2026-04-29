# Chat Models using Google Gemni
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-1-pro')

result = model.invoke('What is the capital of Pakistan?')

print(result.content)