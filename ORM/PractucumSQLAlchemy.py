import sqlalchemy.types
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from typing import Annotated
from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, VARCHAR
from sqlalchemy import Column, REAL , SmallInteger
import datetime
from sqlalchemy.dialects.postgresql import ARRAY


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

    ProductID: Mapped[SmallInteger] = mapped_column(SmallInteger,primary_key=True, autoincrement=True)
    ProductName: Mapped[str] = mapped_column(String(40))
    SupplierID: Mapped[SmallInteger] = mapped_column(SmallInteger)
    CategoryID: Mapped[SmallInteger] = mapped_column(SmallInteger)
    QuantityPerUnit: Mapped[str] = mapped_column(String(20))
    UnitPrice: Mapped[bool] = mapped_column(REAL)
    UnitsInStock: Mapped[SmallInteger] = mapped_column(SmallInteger)
    UnitsOnOrder: Mapped[SmallInteger] = mapped_column(SmallInteger)
    ReorderLevel: Mapped[SmallInteger] = mapped_column(SmallInteger)
    Discontinued: Mapped[int]




BaseTable.metadata.create_all(session.engine)
#BaseTable.metadata.drop_all(session.engine)