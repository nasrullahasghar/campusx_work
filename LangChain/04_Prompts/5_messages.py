import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage,SystemMessage , AIMessage
from dotenv import load_dotenv
load_dotenv()

repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"

llm = HuggingFaceEndpoint(task="text-generation",
                          repo_id = repo_id,
                          max_new_tokens = 500,
                           )
model = ChatHuggingFace(llm=llm)

messages = [
    SystemMessage(content = "You are a very helpful assistsnt"),
    HumanMessage(content = "Tell me about LangChain")
]
result = model.invoke(messages)
messages.append(AIMessage(content = result.content))
print(messages)