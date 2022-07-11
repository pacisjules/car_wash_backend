from fastapi import APIRouter, HTTPException, Depends
from db.table import other_Service_Payment as Osp
from Other_Service_Payment import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()


# All Others Payments
@router.get("/all_other_Payments", response_model=Page[model.Other_Service_Payment_List])
async def find_all_other_Payments(currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):
    query = Osp.select()
    res = await database.fetch_all(query)
    return paginate(res)

#Find one other Payment by ID
@router.get("/other_Payment_by_id/{id}", response_model=model.Other_Service_Payment_List)
async def find_other_Payment_by_id(id: str, currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):
    query = Osp.select().where(Osp.c.id == id)
    return await database.fetch_one(query)

#Find one other Payment by User ID
@router.get("/Payment_by_user_id/{id}", response_model=model.Other_Service_Payment_List)
async def find_other_Payment_by_user_id(id: str, currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):
    query = Osp.select().where(Osp.c.user_id == id)
    return await database.fetch_one(query)


#Find one other Payment by Other Services id
@router.get("/Payment_by_payment_category_id/{id}", response_model=model.Other_Service_Payment_List)
async def find_Payment_by_payment_category_id(id: str, currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):
    query = Osp.select().where(Osp.c.Other_Services_id == id)
    return await database.fetch_one(query)


#Find one other Payment by title
@router.get("/other_Payment_title/{title}", response_model=Page[model.Other_Service_Payment_List])
async def find_like_payment_title(title: str, currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):
    query = "select * from other_Service_Payment where title like '%{}%'".format(title)
    res = await database.fetch_all(query=query, values={})
    return paginate(res)

# Find Payment by status
@router.get("/other_Payment_by_status/{status}", response_model=Page[model.Other_Service_Payment_List])
async def find_other_payment_Payment_by_status(status: str, currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):
    query = Osp.select().where(Osp.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)



# add new Payment
@router.post("/addVehicle_Payment", response_model=model.Other_Service_Payment_List)
async def registerVehicle_Payment(pcg: model.Other_Service_Payment_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = Osp.insert().values(
        
        id = gid,
        user_id=pcg.user_id,

        title=pcg.title,
        description=pcg.description,
        payment_amount=pcg.payment_amount,

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
@router.put("/Vehicle_Payment_update", response_model=model.Other_Service_Payment_List)
async def update_Vehicle_Payment(pcg: model.Other_Service_Payment_Update, currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = Osp.update().where(Osp.c.id == pcg.id).values(
        id = gid,
        user_id=pcg.user_id,

        title=pcg.title,
        description=pcg.description,
        payment_amount=pcg.payment_amount,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_other_Payment_by_id(pcg.id)


#Delete Vehicle_Type
@router.delete("/Delete_payment/{id}", response_model=model.Other_Service_Payment_List)
async def Delete_payment_by__id(id: str, currentUser: model.Other_Service_Payment_List = Depends(util.get_current_active_user)):
    query = Osp.delete().where(Osp.c.id == id)
    return await database.execute(query)