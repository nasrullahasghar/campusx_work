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
chat_history = [SystemMessage(content = "You are a Helpful Assistent")]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input))
    chat_history.append(user_input)
    if user_input == "exit":
        break
    result = model.invoke(user_input)
    chat_history.append(AIMessage(content = result.content))
    print("AI: ",result.content)
print(chat_history)