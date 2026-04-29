# Web Base Loader
import os
os.environ['TRANSFORMERS_VERBOSITY'] = "error"
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

url = "https://tourism.gov.pk/"

loader = WebBaseLoader(url)

load_dotenv()

model = ChatGroq(model_name="llama-3.1-8b-instant")


docs = loader.load()


prompt = PromptTemplate(
    template = "Answer the following question {question} \n from the following text-> \n {text} ",
    input_variables = ['question','text']
)

parser = StrOutputParser()
chain = prompt | model | parser


result = chain.invoke({"question":"What is the name of the Topic in the document","text":docs[0].page_content})

print(result)


