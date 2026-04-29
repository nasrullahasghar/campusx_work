import os
os.environ["TRANSFORMERS_VERBOSITY"] = "error"

from dotenv import load_dotenv
from typing import Optional, Literal
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq

load_dotenv()

# ✅ Updated Groq model (NOT deprecated)
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# ✅ Schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all key themes discussed in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="Return sentiment as 'pos' or 'neg'")
    pros: Optional[list[str]] = Field(default=None, description="List all pros")
    cons: Optional[list[str]] = Field(default=None, description="List all cons")
    name: Optional[str] = Field(default=None, description="Name of the reviewer")

# ✅ Structured Output
structured_model = llm.with_structured_output(Review)

result = structured_model.invoke("""
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse!
The camera is amazing and performance is great.
However, it is heavy and expensive.

Pros:
Powerful processor
Amazing camera
Long battery life

Review by Nitish Singh
""")

print(result)
print("\nSummary:", result.summary)
print("Sentiment:", result.sentiment)
print("Themes:", result.key_themes)
print("Pros:", result.pros)
print("Cons:", result.cons)
print("Reviewer:", result.name)