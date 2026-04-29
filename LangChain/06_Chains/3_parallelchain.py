import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel
load_dotenv()

model1 = ChatGroq(
    model="llama-3.3-70b-versatile",
)

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Meta-Llama-3-8B-Instruct",
    task = "text-generation"
)
model2 = ChatHuggingFace(llm=llm)

prompt1 = PromptTemplate(
    template = "Generate short and simple notes from the following text, \n {text}",
    input_variables = ['text']
)
prompt2 = PromptTemplate(
    template = "Generate 5 questions and answers from the following text, \n {text}",
    input_variables = ['text']
)
prompt3 = PromptTemplate(
    template = "Merge the following notes and quiz into a single document, \n notes-> {notes} and quiz->{quiz}",
    input_variables = ['notes','quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser
})

merged_chain = prompt3 | model1 | parser

chain = parallel_chain | merged_chain

text = """
In machine learning, support vector machines (SVMs, also support vector networks[1]) are supervised max-margin models with associated learning algorithms that analyze data for classification and regression analysis. Developed at AT&T Bell Laboratories,[1][2] SVMs are one of the most studied models, being based on statistical learning frameworks of VC theory proposed by Vapnik (1982, 1995) and Chervonenkis (1974).

In addition to performing linear classification, SVMs can efficiently perform non-linear classification using the kernel trick, representing the data only through a set of pairwise similarity comparisons between the original data points using a kernel function, which transforms them into coordinates in a higher-dimensional feature space. Thus, SVMs use the kernel trick to implicitly map their inputs into high-dimensional feature spaces, where linear classification can be performed.[3] Being max-margin models, SVMs are resilient to noisy data (e.g., misclassified examples). 


The support vector clustering[4] algorithm, created by Hava Siegelmann and Vladimir Vapnik, applies the statistics of support vectors, developed in the support vector machines algorithm, to categorize unlabeled data.[citation needed] These data sets require unsupervised learning approaches, which attempt to find natural clustering of the data into groups, and then to map new data according to these clusters.

The popularity of SVMs is likely due to their amenability to theoretical analysis, and their flexibility in being applied to a wide variety of tasks, including structured prediction problems. It is not clear that SVMs have better predictive performance than other linear models, such as logistic regression and linear regression.[5]
SVMs can be used to solve various real-world problems:

SVMs are helpful in text and hypertext categorization, as their application can significantly reduce the need for labeled training instances in both the standard inductive and transductive settings.[11] Some methods for shallow semantic parsing are based on support vector machines.[12]
Classification of images can also be performed using SVMs. Experimental results show that SVMs achieve significantly higher search accuracy than traditional query refinement schemes after just three to four rounds of relevance feedback. This is also true for image segmentation systems, including those using a modified version SVM that uses the privileged approach as suggested by Vapnik.[13][14]
Classification of satellite data like SAR data using supervised SVM.[15]
Hand-written characters can be recognized using SVM.[16][17]
The SVM algorithm has been widely applied in the biological and other sciences. They have been used to classify proteins with up to 90 percent of the compounds classified correctly. Permutation tests based on SVM weights have been suggested as a mechanism for interpretation of SVM models.[18][19] Support vector machine weights have also been used to interpret SVM models in the past.[20] Posthoc interpretation of support vector machine models in order to identify features used by the model to make predictions is a relatively new area of research with special significance in the biological sciences.
"""

result = chain.invoke({"text":text})
print(result)

chain.get_graph().print_ascii()