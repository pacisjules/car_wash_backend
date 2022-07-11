from fastapi import APIRouter, HTTPException, Depends
from db.table import payment
from Payment import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()

# All Payments
@router.get("/all_Payments", response_model=Page[model.Payment_List])
async def find_all_Payments(currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = payment.select()
    res = await database.fetch_all(query)
    return paginate(res)

#Find one Payment by ID
@router.get("/Payment_by_id/{id}", response_model=model.Payment_List)
async def find_Payment_by_id(id: str, currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = payment.select().where(payment.c.id == id)
    return await database.fetch_one(query)

#Find one Payment by User ID
@router.get("/Payment_by_user_id/{id}", response_model=model.Payment_List)
async def find_payment_Payment_by_user_id(id: str, currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = payment.select().where(payment.c.user_id == id)
    return await database.fetch_one(query)

#Find one Payment by customer id
@router.get("/Payment_by_customer_id/{id}", response_model=model.Payment_List)
async def find_Payment_by_customer_id(id: str, currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = payment.select().where(payment.c.customer_id == id)
    return await database.fetch_one(query)

#Find one Payment by payment category id
@router.get("/Payment_by_payment_category_id/{id}", response_model=model.Payment_List)
async def find_Payment_by_payment_category_id(id: str, currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = payment.select().where(payment.c.payment_category_id == id)
    return await database.fetch_one(query)


#Find one Payment by title
@router.get("/Payment_title/{title}", response_model=Page[model.Payment_List])
async def find_like_payment_Payment(title: str, currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = "select * from payment where title like '%{}%'".format(title)
    res = await database.fetch_all(query=query, values={})
    return paginate(res)

# Find Payment by status
@router.get("/Payment_by_status/{status}", response_model=Page[model.Payment_List])
async def find_payment_Payment_by_status(status: str, currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = payment.select().where(payment.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)



# add new Payment
@router.post("/addVehicle_Payment", response_model=model.Payment_List)
async def registerVehicle_Payment(pcg: model.Payment_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = payment.insert().values(
        
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
@router.put("/Vehicle_Payment_update", response_model=model.Payment_List)
async def update_Vehicle_Payment(pcg: model.Payment_Update, currentUser: model.Payment_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = payment.update().where(payment.c.id == pcg.id).values(
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
    return await find_Payment_by_id(pcg.id)


#Delete Vehicle_Type
@router.delete("/Delete_payment/{id}", response_model=model.Payment_List)
async def Delete_payment_by__id(id: str, currentUser: model.Payment_List = Depends(util.get_current_active_user)):
    query = payment.delete().where(payment.c.id == id)
    return await database.execute(query)