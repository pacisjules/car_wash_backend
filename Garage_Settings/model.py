from pydantic import BaseModel, Field


class Garage_Settings_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    garage_name:str =  Field(..., example="garage name")
    description: str = Field(..., example="description")
    province: str = Field(..., example="province")

    district:str =  Field(..., example="district")
    address:str =  Field(..., example="address")
    office_phone:str =  Field(..., example="office phone")
    mobile_phone:str =  Field(..., example="mobile phone")

    email:str =  Field(..., example="email")
    website:str =  Field(..., example="website")


class Garage_Settings_List(BaseModel):

    id: str

    user_id:str 
    garage_name:str 
    description: str 
    province: str 

    district:str
    address:str 
    office_phone:str 
    mobile_phone:str

    email:str 
    website:str

    status: str
    created_at:str
    last_update_at:str

class Garage_Settings_Update(BaseModel):
    
    id: str

    user_id:str 
    garage_name:str 
    description: str 
    province: str 

    district:str
    address:str 
    office_phone:str 
    mobile_phone:str

    email:str 
    website:str

    status: str
    created_at:str
    last_update_at:str
