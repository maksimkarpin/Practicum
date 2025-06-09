from pydantic import BaseModel
from ORM.Connection import Connection
from ORM.SessionBuilder import SessionBuilder
from ORM.tables.users import Users
from ORM.tables.file_in_users import FilesInMaximus
from ODT.users import UsersDTO
from fastapi import FastAPI, APIRouter
from ORM.BaseTable import BaseTable
import ORM.get as user_get
from sqlalchemy import text

from contextlib import asynccontextmanager
from fastapi import FastAPI

from redis import asyncio as aioredis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

ml_models = {}
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("so_ startup")
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
    BaseTable.metadata.create_all(session.engine)
    redis = aioredis.from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield

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

app = FastAPI(lifespan=lifespan)


app.include_router(user_get.router, tags=['Users'], prefix='/users')
