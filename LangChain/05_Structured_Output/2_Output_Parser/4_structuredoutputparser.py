# It is ajust a topic, and  StructuredOutputParser is removed by LangChain officially
import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()
repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id = repo_id,
    task = "text-generation"
)

model = ChatHuggingFace(llm=llm)

# Schema
schema = [
    ResponseSchema(name = 'fact 1' , description = "Fact 1 about the topic"),
    ResponseSchema(name = 'fact 2' , description = "Fact 2 about the topic"),
    ResponseSchema(name = 'fact 3' , description = "Fact 3 about the topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = "Give 3 facts about the {topic} \n {format_instruction}",
    input_variables = ['topic'],
    partial_variables = {'format_instruction':parser.get_format_instructions()}
)

chian = template | model | parser
prompt = template.invoke({'topic':'pakistan'})
result = model.invoke(prompt)
print(result)