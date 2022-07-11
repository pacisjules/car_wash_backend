from fastapi import APIRouter, HTTPException, Depends
from db.table import garage_Settings
from Garage_Settings import model
from utils import util
from configs.connection import database
import uuid, datetime
from fastapi_pagination import Page, paginate
router = APIRouter()



# All settings
@router.get("/all_settings", response_model=Page[model.Garage_Settings_List])
async def find_all_settings(currentUser: model.Garage_Settings_List = Depends(util.get_current_active_user)):
    query = garage_Settings.select()
    res = await database.fetch_all(query)
    return paginate(res)


#Find settings by ID
@router.get("/other_Service_by_id/{id}", response_model=model.Garage_Settings_List)
async def find_setting_by_id(id: str, currentUser: model.Garage_Settings_List = Depends(util.get_current_active_user)):
    query = garage_Settings.select().where(garage_Settings.c.id == id)
    return await database.fetch_one(query)


# add settings
@router.post("/add_setting", response_model=model.Garage_Settings_List)
async def register_setting(stt: model.Garage_Settings_Create):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())
    query = garage_Settings.insert().values(
        
        id = gid,

        user_id=stt.user_id, 
        garage_name=stt.garage_name, 
        description= stt.description, 
        province= stt.province, 

        district=stt.district,
        address=stt.address, 
        office_phone=stt.office_phone, 
        mobile_phone=stt.mobile_phone,

        email=stt.email, 
        website=stt.website,


        created_at = gdate,
        last_update_at=gdate,
        status = "1"
        
    )

    await database.execute(query)
    return {
        **stt.dict(),
        "id": gid,
        "created_at": gdate,
        "last_update_at": gdate,
        "status": "1"
    }


#Update Vehicle_Type
@router.put("/settings_update", response_model=model.Garage_Settings_List)
async def update_Vehicle_service(stt: model.Garage_Settings_Update, currentUser: model.Garage_Settings_List = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = garage_Settings.update().where(garage_Settings.c.id == stt.id).values(
        id = gid,

        user_id=stt.user_id, 
        garage_name=stt.garage_name, 
        description= stt.description, 
        province= stt.province, 

        district=stt.district,
        address=stt.address, 
        office_phone=stt.office_phone, 
        mobile_phone=stt.mobile_phone,

        email=stt.email, 
        website=stt.website,


        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_setting_by_id(stt.id)


#Delete Vehicle_Type
@router.delete("/Delete_Vehicle_Type/{Vehicle_Type_id}", response_model=model.Garage_Settings_List)
async def Delete_by_Vehicle_Type_id(Vehicle_Type_id: str, currentUser: model.Garage_Settings_List = Depends(util.get_current_active_user)):
    query = garage_Settings.delete().where(garage_Settings.c.id == Vehicle_Type_id)
    return await database.execute(query)