from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str , Field(max_length=50,title="Name of the Patient",description="Give the name of the Patient less then 50 characters",examples=['ALi','Amjad'])]
    email:EmailStr
    linkedin_url:AnyUrl
    age:int = Field(gt=0,lt=120)
    weight: float = Field(gt=0)
    married: Annotated[bool,Field(default=None,description="Is the Patient Married or Not?")]
    allergies: Annotated[Optional[List[str]] , Field(max_length=5)]
    contact_details: Dict[str,str]


def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)

    print("Data Inserted Successfully")
def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.age)
    print(patient.weight)
    print("Data Updated Successfully")

Patient_Info = {'name':"ALI","email":"abc@gmail.com","linkedin_url":"https://poe.com/chat","age":32,"weight":92.4,"married":True,"allergies":['pollen','dust'],"contact_details":{"Phone":"03021312122"}}


Patient1 = Patient(**Patient_Info)
update_patient_data(Patient1)