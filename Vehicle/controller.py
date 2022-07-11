from fastapi import APIRouter, HTTPException, Depends
from db.table import vehicle
from Vehicle import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()

# All Vehicles
@router.get("/all_Vehicles", response_model=Page[model.Vehicle_List])
async def find_all_Vehicles(currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    query = vehicle.select()
    res = await database.fetch_all(query)
    return paginate(res)

#counting all vehicles
@router.get("/count_vehicles")
async def find_all_count(currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    
    query = "SELECT COUNT(id) FROM vehicle"
    res= await database.fetch_all(query=query, values={})
    return res

#Find one Vehicle by ID
@router.get("/Vehicle_ID/{id}", response_model=model.Vehicle_List)
async def find_Vehicle_by_id(id: str, currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    query = vehicle.select().where(vehicle.c.id == id)
    return await database.fetch_one(query)

#Find one Vehicle by car year
@router.get("/Vehicle_year/{year}", response_model=model.Vehicle_List)
async def find_Vehicle_by_id(year: str, currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    query = vehicle.select().where(vehicle.c.car_year== year)
    return await database.fetch_one(query)

#Find one Vehicle by color
@router.get("/Vehicle_color/{color}", response_model=model.Vehicle_List)
async def find_Vehicle_by_id(color: str, currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    query = vehicle.select().where(vehicle.c.car_color == color)
    return await database.fetch_one(query)

#Find one Vehicle by plate
@router.get("/Vehicle_plate/{plate}", response_model=model.Vehicle_List)
async def find_Vehicle_by_id(plate: str, currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    query = vehicle.select().where(vehicle.c.car_plate == plate)
    return await database.fetch_one(query)

# Find Vehicle_Types by status
@router.get("/Vehicle_by_status/{status}", response_model=Page[model.Vehicle_List])
async def find_Vehicle_by_status(status: str, currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    query = vehicle.select().where(vehicle.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new Vehicle_Type
@router.post("/addVehicle", response_model=model.Vehicle_List)
async def registerVehicle(Vhc: model.Vehicle_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = vehicle.insert().values(
        
        id = gid,

        user_id = Vhc.user_id,
        customer_id=Vhc.customer_id,
        vehicle_type_id= Vhc.vehicle_type_id,

       
        car_year=Vhc.car_year, 
        car_color=Vhc.car_color,
        car_plate=Vhc.car_plate,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **Vhc.dict(),
        "id": gid,
        "created_at": gdate,
        "last_update_at": gdate,
        "status": "1"
    }


#Update Vehicle_Type
@router.put("/Vehicle_update", response_model=model.Vehicle_List)
async def update_Vehicle(Vhc: model.Vehicle_Update, currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = vehicle.update().where(vehicle.c.id == Vhc.id).values(
        id = gid,

        user_id = Vhc.user_id,
        customer_id=Vhc.customer_id,
        vehicle_type_id= Vhc.vehicle_type_id,

        
        car_year=Vhc.car_year, 
        car_color=Vhc.car_color,
        car_plate=Vhc.car_plate,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_Vehicle_by_id(Vhc.id)


#Delete Vehicle_Type
@router.delete("/Delete_Vehicle/{Vehicle_Type_id}", response_model=model.Vehicle_List)
async def Delete_by_Vehicle_id(Vehicle_Type_id: str, currentUser: model.Vehicle_List = Depends(util.get_current_active_user)):
    query = vehicle.delete().where(vehicle.c.id == Vehicle_Type_id)
    return await database.execute(query)