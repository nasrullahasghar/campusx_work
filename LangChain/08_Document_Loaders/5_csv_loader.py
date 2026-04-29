# CSV Loader
import os
os.environ['TRANSFORMERS_VERBOSITY'] = "error"
from langchain_community.document_loaders import CSVLoader

data = CSVLoader("Social_Network_Ads.csv")

print(len(data[0]))