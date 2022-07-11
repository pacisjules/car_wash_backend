from fastapi import APIRouter, HTTPException, Depends
from db.table import vehicle_type
from Vehicle_Type import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()


# All Vehicle_Types
@router.get("/all_Vehicle_Types", response_model=Page[model.Vehicle_Type_List])
async def find_allVehicle_Types(currentUser: model.Vehicle_Type_List = Depends(util.get_current_active_user)):
    query = vehicle_type.select()
    res = await database.fetch_all(query)
    return paginate(res)


# Find Vehicle_Types with car brand
@router.get("/Vehicle_Type_brand/{car_brand}", response_model=Page[model.Vehicle_Type_List])
async def find_vehicle_car_brand(car_brand: str, currentUser: model.Vehicle_Type_List = Depends(util.get_current_active_user)):

    query = "select * from vehicle_type where car_brand like '%{}%'".format(car_brand)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)


#counting all vehicle TYPES
@router.get("/count_vehicleTypes")
async def find_all_count(currentUser: model.Vehicle_Type_List = Depends(util.get_current_active_user)):
    
    query = "SELECT COUNT(id) FROM vehicle_type"
    res= await database.fetch_all(query=query, values={})
    return res


#Find one Vehicle_Type by ID
@router.get("/Vehicle_Type/{Vehicle_Type_id}", response_model=model.Vehicle_Type_List)
async def find_Vehicle_Type_by_id(Vehicle_type_id: str, currentUser: model.Vehicle_Type_List = Depends(util.get_current_active_user)):
    query = vehicle_type.select().where(vehicle_type.c.id == Vehicle_type_id)
    return await database.fetch_one(query)

# Find Vehicle_Types by status
@router.get("/Vehicle_Type_by_status/{status}", response_model=Page[model.Vehicle_Type_List])
async def find_Vehicle_Type_by_status(status: str, currentUser: model.Vehicle_Type_List = Depends(util.get_current_active_user)):
    query = vehicle_type.select().where(vehicle_type.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)


# add new Vehicle_Type
@router.post("/addVehicle_Type", response_model=model.Vehicle_Type_List)
async def registerVehicle_Type(Vtp: model.Vehicle_Type_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = vehicle_type.insert().values(
        
        id = gid,

        user_id = Vtp.user_id,
        car_brand = Vtp.car_brand,
        description = Vtp.description,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **Vtp.dict(),
        "id": gid,
        "created_at": gdate,
        "last_update_at": gdate,
        "status": "1"
    }



@router.delete("/delete_vehicle_type/{id}")
async def delete_Vehicle_Type(id:str, currentUser: model.Vehicle_Type_List = Depends(util.get_current_active_user)):
    query = vehicle_type.delete().where(vehicle_type.c.id == id)
    return await database.execute(query)

#Update Vehicle_Type
@router.put("/Vehicle_Type_update", response_model=model.Vehicle_Type_List)
async def update_Vehicle_Type(Vtp: model.Vehicle_Type_Update, currentUser: model.Vehicle_Type_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = vehicle_type.update().where(vehicle_type.c.id == Vtp.id).values(
        id = gid,

        user_id = Vtp.user_id,
        car_brand = Vtp.car_brand,
        description = Vtp.description,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_Vehicle_Type_by_id(Vtp.id)


