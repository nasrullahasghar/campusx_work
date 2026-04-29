import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel , RunnablePassthrough , RunnableLambda
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
def word_count(text):
    return len(text.split(" "))

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "word_count": RunnableLambda(word_count)
})

final_chain = RunnableSequence(joke_gen_chain,parallel_chain)

response = final_chain.invoke({"topic":"Cricket"})
print(f"Joke: {response['joke']} \n Word Count = {response['word_count']}")