from pydantic import BaseModel,EmailStr

class Employeebase(BaseModel):
    name : str
    email : EmailStr

class EmployeeCreate(Employeebase):
    pass

class EmployeeUpdate(Employeebase):
    pass

class EmployeeOut(Employeebase):
    id : int

    class Config:
        orm_mode = True