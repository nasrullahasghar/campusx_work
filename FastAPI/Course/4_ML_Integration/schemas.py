from pydantic import BaseModel,Field,StrictInt,StrictFloat
from typing import Optional ,Literal
class InputSchema(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int = Field(...,ge=0,title="Housing Median Age",description="The Housing Median Age should be greater then 0")
    total_rooms: StrictInt = Field(...,ge=0,title="Total Rooms",description="The Total Rooms should be greater then 0")
    total_bedrooms: StrictInt = Field(...,ge=0,title="Total Bedrooms",description="The Total Bedrooms should be greater then 0")
    population: int = Field(...,ge=0,title="Population",description="The Population should be greater then 0")
    households: StrictInt = Field(...,ge=0,title="Households",description="The Households should be greater then 0")
    median_income: float = Field(...,ge=0,title="Median Income",description="The Median Income should be greater then 0")

class OutputSchema(BaseModel):
    predicted_price: float