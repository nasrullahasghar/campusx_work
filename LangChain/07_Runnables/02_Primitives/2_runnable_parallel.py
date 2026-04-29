import os
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence , RunnableParallel
from langchain_core.prompts import PromptTemplate

load_dotenv()
# Models
model1 = ChatGroq(model_name="llama-3.1-8b-instant")

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Meta-Llama-3-8B-Instruct",
    task = "text-generation"
)
model2 = ChatHuggingFace(llm=llm)
#  Output Parser
parser = StrOutputParser()

# Prompts
prompt1 = PromptTemplate(
    template = "Generate a tweet for topic {topic} ",
    input_variables = ['topic']
)
prompt2 = PromptTemplate(
    template = "Generate a linkedin post for topic {topic} ",
    input_variables = ['topic']
)

# Runnables

parallel_chain = RunnableParallel({
    "tweet": RunnableSequence( prompt1 | model1 | parser),
    "linkedin": RunnableSequence(prompt2 | model2 | parser)
})

result = parallel_chain.invoke({"topic":"AI"})
print('Tweet:\n',result['tweet'])
print('LinkedIn:\n',result['linkedin'])
