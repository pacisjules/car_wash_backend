from fastapi import APIRouter, HTTPException, Depends
from db.table import wash_type
from Wash_type import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()

# All Wash_types
@router.get("/all_Wash_types", response_model=Page[model.Wash_type_List])
async def find_allWash_types(currentUser: model.Wash_type_List = Depends(util.get_current_active_user)):
    query = wash_type.select()
    res = await database.fetch_all(query)
    return paginate(res)

#counting all wash types
@router.get("/count_wash_types")
async def find_all_count(currentUser: model.Wash_type_List = Depends(util.get_current_active_user)):
    
    query = "SELECT COUNT(id) FROM wash_type"
    res= await database.fetch_all(query=query, values={})
    return res



# Find Wash_types with title
@router.get("/Wash_type_title/{title}", response_model=Page[model.Wash_type_List])
async def find_washtype_title(title: str, currentUser: model.Wash_type_List = Depends(util.get_current_active_user)):

    query = "select * from wash_type where title like '%{}%'".format(title)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)

#Find one Wash_type by ID
@router.get("/Wash_type/{Wash_type_id}", response_model=model.Wash_type_List)
async def find_Wash_type_by_id(Wash_type_id: str, currentUser: model.Wash_type_List = Depends(util.get_current_active_user)):
    query = wash_type.select().where(wash_type.c.id == Wash_type_id)
    return await database.fetch_one(query)

# Find Wash_types by status
@router.get("/Wash_type_by_status/{status}", response_model=Page[model.Wash_type_List])
async def find_Wash_type_by_status(status: str, currentUser: model.Wash_type_List = Depends(util.get_current_active_user)):
    query = wash_type.select().where(wash_type.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)


# add new Wash_type
@router.post("/addWash_type", response_model=model.Wash_type_List)
async def registerWash_type(Wtp: model.Wash_type_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = wash_type.insert().values(
        
        id = gid,

        user_id = Wtp.user_id,
        title = Wtp.title,
        description = Wtp.description,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **Wtp.dict(),
        "id": gid,
        "created_at": gdate,
        "last_update_at": gdate,
        "status": "1"
    }


#Update Wash_type
@router.put("/Wash_type_update", response_model=model.Wash_type_List)
async def update_Wash_type(Wtp: model.Wash_type_Update, currentUser: model.Wash_type_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = wash_type.update().where(wash_type.c.id == Wtp.id).values(
        id = gid,

        user_id = Wtp.user_id,
        title = Wtp.title,
        description = Wtp.description,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_Wash_type_by_id(Wtp.id)


#Delete Wash_type
@router.delete("/Delete_Wash_type/{Wash_type_id}", response_model=model.Wash_type_List)
async def Delete_by_Wash_type_id(Wash_type_id: str, currentUser: model.Wash_type_List = Depends(util.get_current_active_user)):
    query = wash_type.delete().where(wash_type.c.id == Wash_type_id)
    return await database.execute(query)