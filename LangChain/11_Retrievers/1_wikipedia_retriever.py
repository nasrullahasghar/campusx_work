import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"
from langchain_community.retrievers import WikipediaRetriever

# Initialize the retriever with the correct language code "en"
retriever = WikipediaRetriever(top_k_results=2, lang="en")

# Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# Get relevant Wikipedia documents
docs = retriever.invoke(query)
for i , doc in enumerate(docs):
    print(f"\n---Result {i+1}---")
    print(f"Page Content:\n{doc.page_content}")