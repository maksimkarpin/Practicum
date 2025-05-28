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
        password = 'Azlk.21412',
        db_name = 'Teach',
        sql_type = "PostgresSQL"
    )
)

class Orders(BaseTable):
    __tablename__ = 'Orders'

    OrderID: Mapped[BaseTable.type_annotation_map['IID']]
    CustomerID: Mapped[str]
    EmployeeID: Mapped[int]
    OrderDate: Mapped[datetime.date]
    RequiredDate: Mapped[datetime.date]
    ShippedDate: Mapped[datetime.date]
    ShipVia: Mapped[str]
    Freight: Mapped[bool] = mapped_column(REAL)
    ShipName: Mapped[str] = mapped_column(String(40))
    ShipAddress: Mapped[str] = mapped_column(String(60))
    ShipCity: Mapped[str] = mapped_column(String(60))
    ShipRegion: Mapped[str] = mapped_column(String(15))
    ShipPostalCode: Mapped[str] = mapped_column(String(10))
    ShipCountry: Mapped[str] = mapped_column(String(10))
    Order: Mapped[list["Products"]] = relationship(back_populates="ProductID")

class Suppliers(BaseTable):
    __tablename__ = 'Suppliers'

    SupplierID: Mapped[BaseTable.type_annotation_map['IID']]
    CompanyName: Mapped[str] = mapped_column(String(40))
    Freight: Mapped[str] = mapped_column(String(40))
    ContactName: Mapped[str] = mapped_column(String(30))
    ContactTitle: Mapped[str] = mapped_column(String(30))
    Address: Mapped[str] = mapped_column(String(60))
    City: Mapped[str] = mapped_column(String(15))
    Region: Mapped[str] = mapped_column(String(15))
    PostalCode: Mapped[str] = mapped_column(String(10))
    Country: Mapped[str] = mapped_column(String(15))
    Phone: Mapped[str] = mapped_column(String(24))
    Fax: Mapped[str] = mapped_column(String(24))
    HomePage: Mapped[int] = mapped_column(server_default=text('0'))

class Products(BaseTable):
    __tablename__ = 'Products'

    ProductID: Mapped[BaseTable.type_annotation_map['IID']]
    ProductName: Mapped[str] = mapped_column(String(40))
    SupplierID: Mapped[int] = mapped_column(SmallInteger)
    CategoryID: Mapped[int] = mapped_column(SmallInteger)
    QuantityPerUnit: Mapped[str] = mapped_column(String(20))
    UnitPrice: Mapped[float]
    UnitsInStock:Mapped[int] = mapped_column(SmallInteger)
    UnitsOnOrder: Mapped[int] = mapped_column(SmallInteger)
    ReorderLevel: Mapped[int] = mapped_column(SmallInteger)
    Discontinued: Mapped[int]
    Product:Mapped[list["Products"]] = relationship(back_populates="SupplierID")

BaseTable.metadata.create_all(session.engine)


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
DownProduct = DownloadSQLProduct()
DownProduct.download_SQL_product(100, 10000)

class ProductODT(BaseModel):
    SKU: int




rs = session.buid().execute(text('select * from "Product"')).all()
for rwo in rs:
    #print(rwo)
    print(ProductODT.model_validate(rwo, from_attributes=True))