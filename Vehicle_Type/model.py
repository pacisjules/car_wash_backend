from pydantic import BaseModel, Field


class Vehicle_Type_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    car_brand:str =  Field(..., example="Names")
    description: str = Field(..., example="bio")

class Vehicle_Type_List(BaseModel):

    id: str

    user_id:str
    car_brand:str
    description: str

    status: str
    created_at:str
    last_update_at:str

class Vehicle_Type_Update(BaseModel):
    
    id: str

    user_id:str
    car_brand:str
    description: str
