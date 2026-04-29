import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()
repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id = repo_id,
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

# Prompt 1 --> Detailed Report
template1 = PromptTemplate(
    template = "Write Detaild report on {topic}",
    input_variables = ['topic']
)
# Prompt 2 --> Summary
template2 = PromptTemplate(
    template = "Write 5 lines summary of the following text. /n{text}",
    input_variables = ['text']
)

prompt1 = template1.invoke({'topic':'blackhole'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})
result2 = model.invoke(prompt2)

print(result2.content)