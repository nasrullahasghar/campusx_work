# TextLoader
import os
os.environ['TRANSFORMERS_VERBOSITY'] = "error"
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model_name="llama-3.1-8b-instant")

loader = TextLoader("cricket.txt", encoding="utf-8")

docs = loader.load()
prompt = PromptTemplate(
    template = "Write a summary of the following poem {poem} \n",
    input_variables = ['poem']
)
parser = StrOutputParser()

chain = prompt | model |  parser
result = chain.invoke({"poem":docs[0].page_content})
print(result)


print(type(docs))
print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

