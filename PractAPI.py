from unicodedata import category
from pydantic import BaseModel
from ORM.Connection import Connection
from ORM.SessionBuilder import SessionBuilder
from ORM.tables.users import Users
from ORM.tables.file_in_users import FilesInMaximus
from ODT.users import UsersDTO
from fastapi import FastAPI, APIRouter
from  ODT.users import UsersDTO
from celery import Celery
import ORM.get as user_get
from sqlalchemy import create_engine, String, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
router = APIRouter()
session = SessionBuilder(
    Connection(
        server="localhost",
        port=5432,
        user='postgres',
        password='Azlk.21412',
        db_name='Teach',
        sql_type="PostgresSQL"
    )
).buid()

app = FastAPI()
class ProdODT(BaseModel):
    __tablename__ = "Product"
    ID: int
    Продавец: str

@router.get('/get')
def run():
    session = SessionBuilder(
        Connection(
            server="localhost",
            port=5432,
            user='postgres',
            password='Azlk.21412',
            db_name='Teach',
            sql_type="PostgresSQL"
        )
    )
    session = session.buid()
    result = session.query(ProdODT).all()
    return result

@router.get('/get_odt', response_model=list[ProdODT])
def run():
    session = SessionBuilder(
        Connection(
            server="localhost",
            port=5432,
            user='postgres',
            password='Azlk.21412',
            db_name='Teach',
            sql_type="PostgresSQL"
        )
    )
    session = session.buid()
    result = session.query(ProdODT).all()
    return result

app.include_router(user_get.router, tags=['Users'], prefix='/users')



