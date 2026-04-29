import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Meta-Llama-3-8B-Instruct",
    task = "text-generation"
)

model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template = "Give me 5 facts in five lines about {topic} ",
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({"topic":"Pakistan"})

print(result)

chain.get_graph().print_ascii()