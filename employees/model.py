from pydantic import BaseModel, Field

class EmployeesCreate(BaseModel):

    user_id:str =  Field(..., example="user id")
    names:str =  Field(..., example="Names")
    bio: str = Field(..., example="bio")
    phone: str = Field(..., example="phone")

    address: str = Field(..., example="address")


class EmployeesList(BaseModel):

    id: str
    user_id:str
    names:str 
    bio: str
    phone: str
    address: str
    
    status: str
    created_at:str
    last_update_at:str

class EmployeesUpdate(BaseModel):
    
    id: str
    user_id:str
    names:str 
    bio: str
    phone: str
    address: str
    
    status: str
    created_at:str
    last_update_at:str

