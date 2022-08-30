import sqlalchemy
from sqlalchemy import ForeignKey
metadata = sqlalchemy.MetaData()

#Start and Configuration


#1 Table App Admins
users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String, unique=True),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    
    sqlalchemy.Column("first_name"  , sqlalchemy.String),
    sqlalchemy.Column("last_name"  , sqlalchemy.String),


    sqlalchemy.Column("email"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("type"     , sqlalchemy.String),
    sqlalchemy.Column("role"     , sqlalchemy.String),

    sqlalchemy.Column("company"     , sqlalchemy.String),
    sqlalchemy.Column("phone"     , sqlalchemy.String, unique=True),
    sqlalchemy.Column("living"     , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#2 Table Customers
customer  = sqlalchemy.Table(
    "customer",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("names"  , sqlalchemy.String),
    sqlalchemy.Column("tin"  , sqlalchemy.String),

    sqlalchemy.Column("bio"    , sqlalchemy.String),
    sqlalchemy.Column("email"  , sqlalchemy.String),
    sqlalchemy.Column("phone"  , sqlalchemy.String),
    sqlalchemy.Column("province"    , sqlalchemy.String),
    sqlalchemy.Column("district"    , sqlalchemy.String),
    sqlalchemy.Column("address"    , sqlalchemy.String),
    sqlalchemy.Column("identity_number"  , sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("qr_name"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#3 Table Vehicle Type
vehicle_type  = sqlalchemy.Table(
    "vehicle_type",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),

    sqlalchemy.Column("car_brand"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#4 Table Vehicle
vehicle  = sqlalchemy.Table(
    "vehicle",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("customer_id", sqlalchemy.String, ForeignKey(customer.c.id), nullable=False),
    sqlalchemy.Column("vehicle_type_id", sqlalchemy.String, ForeignKey(vehicle_type.c.id), nullable=False),

    
    sqlalchemy.Column("car_year"  , sqlalchemy.String),
    sqlalchemy.Column("car_color"  , sqlalchemy.String),
    sqlalchemy.Column("car_plate"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#5 Table Wash type
wash_type  = sqlalchemy.Table(
    "wash_type",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),


    sqlalchemy.Column("title"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)




#6 Table Service
service  = sqlalchemy.Table(
    "service",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("customer_id", sqlalchemy.String, ForeignKey(customer.c.id), nullable=False),
    sqlalchemy.Column("vehicle_id", sqlalchemy.String, ForeignKey(vehicle.c.id), nullable=False),
    sqlalchemy.Column("wash_type_id", sqlalchemy.String, ForeignKey(wash_type.c.id), nullable=False),


    sqlalchemy.Column("comment"  , sqlalchemy.String),
    sqlalchemy.Column("price"  , sqlalchemy.Float),
    sqlalchemy.Column("service_identity"  , sqlalchemy.String, nullable=False, unique=True),
    sqlalchemy.Column("qr_name"  , sqlalchemy.String),
    sqlalchemy.Column("process_level"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),


    sqlalchemy.Column("month"  , sqlalchemy.Integer),
    sqlalchemy.Column("year"  , sqlalchemy.Integer),

)


#8 Table Other_Services
other_Services  = sqlalchemy.Table(
    "other_Services",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("customer_id", sqlalchemy.String, ForeignKey(customer.c.id), nullable=False),
    sqlalchemy.Column("vehicle_id", sqlalchemy.String, ForeignKey(vehicle.c.id), nullable=False),

    sqlalchemy.Column("title"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("unit_price"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


#9 Table payment_type
payment_category  = sqlalchemy.Table(
    "payment_category",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),

    sqlalchemy.Column("title"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("schedule_type"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)

#10 Table payment_type
payment  = sqlalchemy.Table(
    "Payment",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("payment_category_id", sqlalchemy.String, ForeignKey(payment_category.c.id), nullable=False),
    sqlalchemy.Column("customer_id", sqlalchemy.String, ForeignKey(customer.c.id), nullable=False),

    sqlalchemy.Column("title"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("payment_amount"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


# RESUME JOBS

#11 Table Other service payment_type
other_Service_Payment  = sqlalchemy.Table(
    "Other_Service_Payment",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("Other_Services_id", sqlalchemy.String, ForeignKey(payment_category.c.id), nullable=False),
    sqlalchemy.Column("customer_id", sqlalchemy.String, ForeignKey(customer.c.id), nullable=False),

    sqlalchemy.Column("title"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("payment_type"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)



#12 Table Garage Settings
garage_Settings  = sqlalchemy.Table(
    "garage_Settings",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),

    sqlalchemy.Column("garage_name"  , sqlalchemy.String),
    sqlalchemy.Column("description"  , sqlalchemy.String),
    sqlalchemy.Column("province"    , sqlalchemy.String),
    sqlalchemy.Column("district"    , sqlalchemy.String),
    sqlalchemy.Column("address"  , sqlalchemy.String),
    sqlalchemy.Column("office_phone"  , sqlalchemy.String),
    sqlalchemy.Column("mobile_phone"  , sqlalchemy.String),
    sqlalchemy.Column("email"  , sqlalchemy.String),
    sqlalchemy.Column("website"  , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)



#13 Table account recovery Keys
account_keys  = sqlalchemy.Table(
    "account_keys",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),

    sqlalchemy.Column("key"  , sqlalchemy.String, unique=True, nullable=False),
    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
)


#14 Table Customers
employees  = sqlalchemy.Table(
    "employees",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String , primary_key=True),
    sqlalchemy.Column("user_id", sqlalchemy.String, ForeignKey(users.c.id), nullable=False),
    sqlalchemy.Column("names"  , sqlalchemy.String),

    sqlalchemy.Column("bio"    , sqlalchemy.String),
    sqlalchemy.Column("phone"  , sqlalchemy.String),
    sqlalchemy.Column("address"    , sqlalchemy.String),

    sqlalchemy.Column("status"    , sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.String),
    sqlalchemy.Column("last_update_at", sqlalchemy.String),
)


