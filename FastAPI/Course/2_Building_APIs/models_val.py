from pydantic import BaseModel,Field,StrictInt
from typing import Optional


class Employee(BaseModel):
    id: int = Field(...,gt=0,title="ID of the Employee")
    name: str = Field(...,min_length=3,max_length=30,title="Name of the Employee")
    department: str = Field(...,min_length=3,max_length=40,title="Department of the Employee")
    age: Optional[StrictInt] = Field(default=None,ge=18,title="Age of the Employee",description="The Age of the employee should be Greater then and equal to 18")