from pydantic import BaseModel, Field


class Payment_category_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    title:str =  Field(..., example="title")
    description:str =  Field(..., example="description")
    schedule_type:str =  Field(..., example="Schedule type")



class Payment_category_List(BaseModel):

    id: str

    user_id:str
    title:str
    description:str
    schedule_type:str

    status: str
    created_at:str
    last_update_at:str

class Payment_category_Update(BaseModel):
    
    id: str

    user_id:str
    title:str
    description:str
    schedule_type:str

    status: str
    created_at:str
    last_update_at:str
