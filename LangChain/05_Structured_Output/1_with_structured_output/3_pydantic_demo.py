from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str = 'nitish'
    age: Optional[int] = None
    email: EmailStr
    cgpa:float = Field(gt=0,lt=4.0,description='The CGPA should be b/w 0 t0 4.0')

new_student = {'age':'32','email':'abc@gmail.com','cgpa':3.2}

student = Student(**new_student)
# We can make it Dictionary
student_dict = dict(student)
# We can make it Json
student_json = student.model_dump_json()

# Dict calling
print(student.name)

print(student)