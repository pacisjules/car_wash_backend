from pydantic import BaseModel, Field


class Payment_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    payment_category_id:str =  Field(..., example="payment category id")
    customer_id:str =  Field(..., example="customer id")

    title:str =  Field(..., example="title")
    description:str =  Field(..., example="description")
    payment_amount:str =  Field(..., example="payment amount")



class Payment_List(BaseModel):

    id: str

    user_id:str
    payment_category_id:str 
    customer_id:str 

    title:str
    description:str
    payment_amount:str

    status: str
    created_at:str
    last_update_at:str

class Payment_Update(BaseModel):
    
    id: str

    user_id:str
    payment_category_id:str 
    customer_id:str 

    title:str
    description:str
    payment_amount:str

    status: str
    created_at:str
    last_update_at:str
