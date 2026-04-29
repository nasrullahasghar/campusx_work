import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"

llm = HuggingFaceEndpoint(
    repo_id = repo_id,
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

template1 = PromptTemplate(
    template = "Write a Detail report on {topic}",
    input_variables = ['topic']
)

template2 = PromptTemplate(
    template = "Give me a five line Summary of the following text. /n{text}",
    input_variables = ['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic":"Gaza genocide"})
print(result)