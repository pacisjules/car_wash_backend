from fastapi import APIRouter, HTTPException, Depends
from db.table import payment_category as paca
from Payment_category import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()



# All Payment_categories
@router.get("/all_Payment_category", response_model=Page[model.Payment_category_List])
async def find_all_category_Type(currentUser: model.Payment_category_List = Depends(util.get_current_active_user)):
    query = paca.select()
    res = await database.fetch_all(query)
    return paginate(res)


#Find one category by ID
@router.get("/category_by_id/{id}", response_model=model.Payment_category_List)
async def find_category_by_id(id: str, currentUser: model.Payment_category_List = Depends(util.get_current_active_user)):
    query = paca.select().where(paca.c.id == id)
    return await database.fetch_one(query)


#Find one category by User ID
@router.get("/payment_category_by_user_id/{id}", response_model=model.Payment_category_List)
async def find_payment_category_by_user_id(id: str, currentUser: model.Payment_category_List = Depends(util.get_current_active_user)):
    query = paca.select().where(paca.c.user_id == id)
    return await database.fetch_one(query)

#Find one category by title
@router.get("/payment_category_title/{title}", response_model=Page[model.Payment_category_List])
async def find_like_payment_category(title: str, currentUser: model.Payment_category_List = Depends(util.get_current_active_user)):
    query = "select * from payment_category where title like '%{}%'".format(title)
    res = await database.fetch_all(query=query, values={})
    return paginate(res)


# Find category by status
@router.get("/payment_category_by_status/{status}", response_model=Page[model.Payment_category_List])
async def find_payment_category_by_status(status: str, currentUser: model.Payment_category_List = Depends(util.get_current_active_user)):
    query = paca.select().where(paca.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)



# add new category
@router.post("/addVehicle_paca", response_model=model.Payment_category_List)
async def registerVehicle_paca(pcg: model.Payment_category_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = paca.insert().values(
        
        id = gid,
        user_id=pcg.user_id,

        title=pcg.title,
        description=pcg.description,
        schedule_type=pcg.schedule_type,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **pcg.dict(),
        "id": gid,
        "created_at": gdate,
        "last_update_at": gdate,
        "status": "1"
    }


#Update Vehicle_Type
@router.put("/Vehicle_paca_update", response_model=model.Payment_category_List)
async def update_Vehicle_paca(pcg: model.Payment_category_Update, currentUser: model.Payment_category_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = paca.update().where(paca.c.id == pcg.id).values(
        id = gid,
        user_id=pcg.user_id,

        title=pcg.title,
        description=pcg.description,
        schedule_type=pcg.schedule_type,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_category_by_id(pcg.id)


#Delete Vehicle_Type
@router.delete("/Delete_payment_category/{Vehicle_Type_id}", response_model=model.Payment_category_List)
async def Delete_payment_category_by__id(Vehicle_Type_id: str, currentUser: model.Payment_category_List = Depends(util.get_current_active_user)):
    query = paca.delete().where(paca.c.id == Vehicle_Type_id)
    return await database.execute(query)