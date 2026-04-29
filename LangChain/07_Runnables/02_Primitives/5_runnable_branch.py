import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableBranch
from langchain_core.prompts import PromptTemplate

load_dotenv()
# Models
model = ChatGroq(model_name="llama-3.1-8b-instant")

prompt1 = PromptTemplate(
    template = "Write a detailed note on {topic}",
    input_variales = ['topic']
)

prompt2 = PromptTemplate(
    template = "Generate a summary of the following text, \n{text}",
    input_variales = ['text']
)

parser = StrOutputParser()

report_gen_chain = prompt1 | model | parser # RunnableSequence using LCEL 

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 300 ,prompt2 | model | parser), # RunnableSequence using LCEL ) 
    (RunnablePassthrough())
)

final_chain = report_gen_chain | branch_chain # RunnableSequence using LCEL 

result = final_chain.invoke({"topic":"Pakistan Vs India Wars"})

print(result)