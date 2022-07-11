import databases
import sqlalchemy
from functools import lru_cache
from configs import dbinfo
from db.table import metadata

@lru_cache()
def db_config():
    return dbinfo.Setting()

def DATABASE_URL(
    connection: str = "postgresql",
    username: str   = "nljrgdamgfpuxk",
    password: str   ="86b08808d0141eab85ac115f7cce5cd408f574728438d42d1ed3fa5add0df0fb",
    host: str       = "127.0.0.1",
    port: str       = "5432", #5432 always for postgress
    database: str   = "car_wash"
):
    return str(connection+"://nljrgdamgfpuxk:86b08808d0141eab85ac115f7cce5cd408f574728438d42d1ed3fa5add0df0fb@ec2-3-222-74-92.compute-1.amazonaws.com:5432/d3q8kc6m257chd")

database = databases.Database(DATABASE_URL())

engine = sqlalchemy.create_engine(
    DATABASE_URL()
)

metadata.create_all(engine)