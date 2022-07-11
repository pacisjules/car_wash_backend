from configs.connection import database
from fastapi import FastAPI, Depends, Request
from functools import lru_cache
from configs import appinfo
import time
from fastapi_pagination import add_pagination
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

now = datetime.now()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/image", tags=["image Reader"])
async def main_Image():
    return FileResponse("auth/qrkey/qr1.png")


@app.get("/", tags=["Root"])
async def root():
    return{
        "message": "This Apis for Car Wash System",
        "Software Engineer": "ISHIMWE JULES Pacis",
        "Email": "ishimwejulespacis@gmail.com",
        "GitHub": "https://github.com/pacisjules",
        "owner_name"    :"NTIGURIRWA Barnabe",
    }


@app.get("/app/info", tags=["App"])
async def app_info():
    return {
        "app_name"      : "Car Wash Platform",
        "app_version"   : "1.0",
        "app_framework" : "FastAPI (Python)",
        "status" : "Building process...",
        "app_date_now"  : now.strftime("%Y-%m-%d %H:%M:%S"),
        "owner_name"    :"NTIGURIRWA Barnabe",
    }


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)

    return response


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


from auth import controller as authController
from users import controller as userController
from customer import controller as customerController

from Garage_Settings import controller as garageController
from Vehicle_Type import controller as vehicletypeController
from Vehicle import controller as vehicleController
from Wash_type import controller as washtypeController
from Service import controller as serviceController
from Payment_category import controller as payment_categoryController
from Payment import controller as paymentController
from Other_Services import controller as otherserviceController
from Other_Service_Payment import controller as otherservicepaymentController

#Config Parts
app.include_router(authController.router, tags=["Auth"])
app.include_router(userController.router, tags=["Users"])
app.include_router(garageController.router, tags=["Settings"])

#Application Parts
app.include_router(customerController.router, tags=["Customers"])
app.include_router(vehicletypeController.router, tags=["Vehicle Type"])
app.include_router(vehicleController.router, tags=["Vehicle"])
app.include_router(washtypeController.router, tags=["Wash Type"])
app.include_router(serviceController.router, tags=["Service"])

app.include_router(payment_categoryController.router, tags=["Payment Category"])
app.include_router(paymentController.router, tags=["Payment"])
app.include_router(otherserviceController.router, tags=["Other Services"])
app.include_router(otherservicepaymentController.router, tags=["Other Services Payment"])

add_pagination(app)