from pydantic import BaseModel, Field


class Other_Service_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    customer_id:str =  Field(..., example="customer id")
    vehicle_id:str =  Field(..., example="vehicle id")

    title:str =  Field(..., example="title")
    description:str =  Field(..., example="description")
    unit_price:str =  Field(..., example="unit price")


class Other_Service_List(BaseModel):

    id: str

    user_id:str
    customer_id:str 
    vehicle_id:str

    title:str 
    description:str 
    unit_price:str 


    status: str
    created_at:str
    last_update_at:str

class Other_Service_Update(BaseModel):
    
    id: str

    user_id:str
    customer_id:str 
    vehicle_id:str

    title:str 
    description:str 
    unit_price:str 


    status: str
    created_at:str
    last_update_at:str
