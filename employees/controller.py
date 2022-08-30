from fastapi import APIRouter, HTTPException, Depends
from db.table import employees
from employees import model
from utils import util
from configs.connection import database
import uuid, datetime



from fastapi_pagination import Page, paginate
router = APIRouter()


# All employeess
@router.get("/all_employeess", response_model=Page[model.EmployeesList])
async def find_allemployees(currentUser: model.EmployeesList = Depends(util.get_current_active_user)):
    query = employees.select().order_by(employees.c.id.desc())
    res = await database.fetch_all(query)
    return paginate(res)

# Find employeess with names
@router.get("/like_employees/{names}", response_model=Page[model.EmployeesList])
async def find_like_employees(names: str, currentUser: model.EmployeesList = Depends(util.get_current_active_user)):

    query = "select * from employees where names like '%{}%'".format(names)
    res= await database.fetch_all(query=query, values={})
    return paginate(res)


#counting all employeess
@router.get("/count_employeess")
async def count_all_count(currentUser: model.EmployeesList = Depends(util.get_current_active_user)):
    query = "SELECT COUNT(id) FROM employees"
    res= await database.fetch_all(query=query, values={})
    return res


#Find one employees by ID
@router.get("/employees/{employees_id}", response_model=model.EmployeesList)
async def find_employees_by_id(employees_id: str, currentUser: model.EmployeesList = Depends(util.get_current_active_user)):
    query = employees.select().where(employees.c.id == employees_id)
    return await database.fetch_one(query)


# Find employeess by phone
@router.get("/find_employees_by_phone/{phone}", response_model=Page[model.EmployeesList])
async def find_employeess_by_phone(phone: str, currentUser: model.EmployeesList = Depends(util.get_current_active_user)):
    query = employees.select().where(employees.c.phone == phone)
    res = await database.fetch_all(query)
    return paginate(res)


# Find employeess by status
@router.get("/employees_by_status/{status}", response_model=Page[model.EmployeesList])
async def find_employees_by_status(status: str, currentUser: model.EmployeesList = Depends(util.get_current_active_user)):
    query = employees.select().where(employees.c.status == status)
    res = await database.fetch_all(query)
    return paginate(res)

# add new employees
@router.post("/addemployees")
async def register_employees(employeess: model.EmployeesCreate):
    
    # check if employees already exists
    Cquery = employees.select().where(employees.c.phone == employeess.phone)
    Cres = await database.fetch_one(Cquery)
    if Cres:
        return{
            "message": "employee "+employeess.names+" already exists",
            "status": 0
        }
    else:

        gid = str(uuid.uuid1())
        gdate = str(datetime.datetime.now())

        #Adding employees
        query = employees.insert().values(
            
            id = gid,
            
            user_id=employeess.user_id,
            names=employeess.names, 
            bio= employeess.bio,
            phone= employeess.phone,
            TypeChoosen=employees.TypeChoosen,

            address= employeess.address,

            created_at = gdate,
            last_update_at=gdate,
            status = "1"
        )

        await database.execute(query)

        return{
            "Message":employeess.names+" has been registered",
            "Email":"Email sent",
            "status": 1
        }


#Update employees
@router.put("/employees_update", response_model=model.EmployeesList)
async def update_employees(Empl: model.EmployeesUpdate, currentUser: model.EmployeesList = Depends(util.get_current_active_user)):

    gid = str(uuid.uuid1())
    gdate = str(datetime.datetime.now())

    Query = employees.update().where(employees.c.id == Empl.id).values(
        id = gid,

        user_id=Empl.user_id,
        names=Empl.names, 
        bio= Empl.bio,
        phone= Empl.phone,
        TypeChoosen=Empl.TypeChoosen,

        address= Empl.address,

        created_at = gdate,
        last_update_at=gdate,
        status = "1"
    )

    await database.execute(Query)
    return await find_employees_by_id(Empl.id)


#Delete employees
@router.delete("/Delete_employees/{employees_id}", response_model=model.EmployeesList)
async def Delete_by_employees_id(employees_id: str, currentUser: model.EmployeesList = Depends(util.get_current_active_user)):
    query = employees.delete().where(employees.c.id == employees_id)
    return await database.execute(query)