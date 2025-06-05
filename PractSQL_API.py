from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from sqlalchemy import text, BIGINT
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, VARCHAR
from sqlalchemy import Column, REAL , SmallInteger
from abc import abstractmethod
import pandas as pd
import requests
from io import BytesIO
import datetime
from sqlalchemy import create_engine
from pydantic import BaseModel
from fastapi import FastAPI

class Connection:
    def __init__(self, sql_type, user, password, server, port = None, **args) -> None:
        self.user = user
        self.password = password
        self.server = server
        self.port = port
        self.sql_type = sql_type
        self.args = args

    @property
    def engin(self):
        if self.sql_type == "MSSQL":
            return f"mssql+pymssql://{self.user}:{ self.password}@{self.server}/{self.args['db_name']}"
        if self.sql_type == "PostgresSQL":
            return f"postgresql://{self.user}:{self.password}@{self.server}:{str(self.port)}/{self.args['db_name']}"
        else: print("Not connections")


class SessionBuilder:

    def __init__(self, connection: Connection)->None:
        self.engine  = create_engine(connection.engin)

    def buid(self):
        Session = sessionmaker (bind = self.engine)
        return Session()


class BaseTable(DeclarativeBase):
    __abstract__ = True

    type_annotation_map = {
        "IID": Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
    }

    def __init__(self, **args):
        columns = self.__table__.c.keys()
        for key, value in args.items():
            if key in columns: setattr(self, key, value)


session = SessionBuilder(
    Connection(
        server="localhost",
        port = 5432 ,
        user = 'postgres',
        password = 'password',
        db_name = 'Teach',
        sql_type = "PostgresSQL"
    )
)

class Method:
    url = 'https://analitika.woysa.club/images/panel/json/download/niches.php'
    def __init__(self,skip, category):
        self.skip = skip
        self.category = category
    @abstractmethod
    def download(self, skip, category):
        ...

class DownloadSQLProduct(Method):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'inst'):
            cls.obj = range(0, 1000)
            cls.inst = super(DownloadSQLProduct, cls).__new__(cls)
        return cls.inst

    def __init__(self):
        ...

    def download_SQL_product(self,skip, category):
        url = self.url + f"?skip={skip}&price_min=0&price_max=1060225&up_vy_min=0&up_vy_max=108682515&up_vy_pr_min=0&up_vy_pr_max=2900&sum_min=1000&sum_max=82432725&feedbacks_min=0&feedbacks_max=32767&trend=false&sort=sum_sale&sort_dir=-1&id_cat={category}"
        response = requests.get(url)
        df = pd.read_excel(BytesIO(response.content), engine='openpyxl')
        df['category_id'], df['download_date'] = category, datetime.datetime.now()
        engine = create_engine(f"postgresql://postgres:Azlk.21412@localhost:5432/Teach")
        connection1 = engine.connect()
        df.to_sql('Product', connection1, if_exists='replace', index=False)
        rs = session.buid().execute(text('select * from "Product"'))
        #for record in rs:
            #print(record)
#DownProduct = DownloadSQLProduct()
#DownProduct.download_SQL_product(700, 10000)

class ProductODTSellers(BaseModel):
    Продавец: str

class ProductODTSellers_ID(BaseModel):
    SKU: int
    Продавец: str




app=FastAPI()


rs = session.buid().execute(text('select *  from "Product"')).all()


@app.get("/sallers")
def sellers():
    sellers = []
    for rwo in rs:
        db = ProductODTSellers.model_validate(rwo, from_attributes=True)
        sellers.append(db)
    return sellers
@app.get(f"/sallers/SKU/")
def sellers_id():
    SKU = 252338777

    sellers_id = []
    rs = session.buid().execute(text('select "SKU", "Продавец"  from "Product"')).all()
    for rwo in rs:
        if SKU in rwo:


            db = ProductODTSellers_ID.model_validate(rwo, from_attributes=True)
            sellers_id.append(db)




    return sellers_id


