import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough
from langchain_core.prompts import PromptTemplate

load_dotenv()
# Models
model = ChatGroq(model_name="llama-3.1-8b-instant")


prompt1 = PromptTemplate(
    template = "Write a joke about {topic}",
    input_variables = ['topic']
)
prompt2 = PromptTemplate(
    template = "Explain the following joke - {text}",
    input_variables = ['text']
)

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1 , model , parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(prompt2, model ,parser)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

response = final_chain.invoke({"topic":"Cricket"})
print(response)