# Maximum Marginal Relevence (MMR)

from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Step 1: Your source documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

# Step 2: Initialize embedding model
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Step 3: Create FIASS vector store in memory
vectorstore = FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

# Step 4: Convert vectorstore into a retriever
retriever  = vectorstore.as_retriever(
    search_type = "mmr",     # <--- This enables MMR 
    search_kwargs = {"k":3, "lambda_mult": 0.5} # k = top results, lambda_mult = relevance-diversity balance
)

query = "What is langchain?"
results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)