from pydantic import BaseModel, Field


class Other_Service_Payment_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    Other_Services_id:str =  Field(..., example="Other Services id")

    title:str =  Field(..., example="title")
    description:str =  Field(..., example="description")
    payment_amount:str =  Field(..., example="payment amount")



class Other_Service_Payment_List(BaseModel):

    id: str

    user_id:str
    payment_category_id:str 

    title:str
    description:str
    payment_amount:str

    status: str
    created_at:str
    last_update_at:str

class Other_Service_Payment_Update(BaseModel):
    
    id: str

    user_id:str
    payment_category_id:str 


    title:str
    description:str
    payment_amount:str

    status: str
    created_at:str
    last_update_at:str
