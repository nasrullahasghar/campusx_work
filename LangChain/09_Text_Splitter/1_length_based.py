# Length Based Text Splitter
import os
os.environ['TRANSFORMERS_VERBOSITY'] = "error"
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

loader = PyPDFLoader("dl-curriculum.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=""
)

result = splitter.split_documents(docs)
print(result[1].page_content)

