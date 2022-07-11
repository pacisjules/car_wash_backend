from fastapi import APIRouter, HTTPException, Depends
from db.table import other_Services as Service
from Other_Services import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()



# All Other services
@router.get("/all_Other_services", response_model=Page[model.Other_Service_List])
async def find_all_other_services(currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):
    query = Service.select()
    res = await database.fetch_all(query)
    return paginate(res)


#Find one other Service by ID
@router.get("/other_Service_by_id/{id}", response_model=model.Other_Service_List)
async def find_other_service_by_id(id: str, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):
    query = Service.select().where(Service.c.id == id)
    return await database.fetch_one(query)

#Find one other Service by User ID
@router.get("/other_Service_by_user_id/{id}", response_model=model.Other_Service_List)
async def find_other_service_by_user_id(id: str, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):
    query = Service.select().where(Service.c.user_id == id)
    return await database.fetch_one(query)


#Find one Payment by customer id
@router.get("/Other_service_by_customer_id/{id}", response_model=model.Other_Service_List)
async def find_other_service_by_customer_id(id: str, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):
    query = Service.select().where(Service.c.customer_id == id)
    return await database.fetch_one(query)


#Find one Payment by vehicle id
@router.get("/Other_service_by_customer_id/{id}", response_model=model.Other_Service_List)
async def find_other_service_by_customer_id(id: str, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):
    query = Service.select().where(Service.c.customer_id == id)
    return await database.fetch_one(query)




#Find one other Service by title
@router.get("/other_service_like_title/{title}", response_model=Page[model.Other_Service_List])
async def find_like_movie(title: str, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):

    query = "select * from other_Services where title like '%{}%'".format(title)
    res = await database.fetch_all(query=query, values={})
    return paginate(res)

# Find other service by status
@router.get("/other_service_by_status/{status}", response_model=Page[model.Other_Service_List])
async def find_other_service_by_status(status: str, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):
    query = Service.select().where(Service.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new other Service
@router.post("/addOther_service", response_model=model.Other_Service_List)
async def registerVehicle_service(vsr: model.Other_Service_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = Service.insert().values(
        
        id = gid,
        user_id=vsr.user_id,
        customer_id=vsr.customer_id,
        vehicle_id=vsr.vehicle_id,

        title=vsr.title,
        description=vsr.description,
        unit_price=vsr.unit_price,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **vsr.dict(),
        "id": gid,
        "created_at": gdate,
        "last_update_at": gdate,
        "status": "1"
    }


#Update Vehicle_Type
@router.put("/Vehicle_service_update", response_model=model.Other_Service_List)
async def update_Vehicle_service(vsr: model.Other_Service_Update, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = Service.update().where(Service.c.id == vsr.id).values(
        id = gid,
        user_id=vsr.user_id,
        customer_id=vsr.customer_id,
        vehicle_id=vsr.vehicle_id,

        title=vsr.title,
        description=vsr.description,
        unit_price=vsr.unit_price,


        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_other_service_by_id(vsr.id)


#Delete Vehicle_Type
@router.delete("/Delete_Vehicle_Type/{Vehicle_Type_id}", response_model=model.Other_Service_List)
async def Delete_by_Vehicle_Type_id(Vehicle_Type_id: str, currentUser: model.Other_Service_List = Depends(util.get_current_active_user)):
    query = Service.delete().where(Service.c.id == Vehicle_Type_id)
    return await database.execute(query)