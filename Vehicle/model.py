from pydantic import BaseModel, Field


class Vehicle_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    customer_id:str =  Field(..., example="customer id")
    vehicle_type_id: str = Field(..., example="vehicle type id")

    car_year:str =  Field(..., example="car year")
    car_color:str =  Field(..., example="car color")
    car_plate:str =  Field(..., example="car plate")


class Vehicle_List(BaseModel):

    id: str

    user_id:str 
    customer_id:str
    vehicle_type_id: str 


    car_year:str 
    car_color:str
    car_plate:str

    status: str
    created_at:str
    last_update_at:str

class Vehicle_Update(BaseModel):
    
    id: str

    user_id:str 
    customer_id:str
    vehicle_type_id: str 


    car_year:str 
    car_color:str
    car_plate:str

