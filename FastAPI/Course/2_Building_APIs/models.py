from pydantic import BaseModel,Field
from typing import Optional


class Employee(BaseModel):
    id: int 
    name: str
    department: str
    age: int
    