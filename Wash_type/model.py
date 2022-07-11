from pydantic import BaseModel, Field


class Wash_type_Create(BaseModel):
    
    user_id:str =  Field(..., example="user id")
    title:str =  Field(..., example="Names")
    description: str = Field(..., example="bio")

class Wash_type_List(BaseModel):

    id: str
    user_id:str
    title:str
    description: str

    status: str
    created_at:str
    last_update_at:str

class Wash_type_Update(BaseModel):
    
    id: str
    user_id:str
    title:str
    description: str


