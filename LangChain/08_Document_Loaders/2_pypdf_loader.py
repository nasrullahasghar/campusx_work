# PyPDF Loader
import os
os.environ['TRANSFORMERS_VERBOSITY'] = "error"
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load() # Loads all documents at once in memory

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)