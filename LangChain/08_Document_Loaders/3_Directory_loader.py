# Directory Loader
import os
os.environ['TRANSFORMERS_VERBOSITY'] = "error"
from langchain_community.document_loaders import TextLoader , PyPDFLoader , DirectoryLoader


loader = DirectoryLoader(
    path = "books",
    glob = "*.pdf",
    loader_cls = PyPDFLoader
)

docs = loader.lazy_load() # Loads one document at a time in memory

for documant in docs:
    print(documant.metadata)
