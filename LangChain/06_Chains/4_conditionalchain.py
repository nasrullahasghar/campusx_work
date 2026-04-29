import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser,StrOutputParser
from langchain_core.runnables import RunnableBranch , RunnableParallel , RunnableLambda
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal
load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description = "Give the sentiment of the feedback")


parser2 = PydanticOutputParser(pydantic_object = Feedback)

prompt1 = PromptTemplate(
    template = "Classify the sentiment of the following  text into positive and negative, \n{feedback}, \n {format_instruction}",
    input_variables =  ['feedback'],
    partial_variables = {"format_instruction":parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = "Give an appropriate response to this positive feedback \n {feedback}",
    input_variables = ['feedback']
)
prompt3 = PromptTemplate(
    template = "Give an appropriate response to this negative feedback \n {feedback}",
    input_variables = ['feedback']
)
branch_chain = RunnableBranch(
    (lambda x:x.sentiment == "positive", prompt2 | model | parser),
    (lambda x:x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find sentiment")
)

chain = classifier_chain | branch_chain
result = chain.invoke({"feedback": "This phone includes some positive features and some negative features"})
print(result)
