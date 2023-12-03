import uvicorn
from microshop.core.config import settings
from fastapi import FastAPI
from contextlib import asynccontextmanager
from item_rst import items_rst
from microshop.users.views import users_rst
from microshop.core.models import Base, db_helper
from microshop.api_v1 import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(items_rst)
app.include_router(users_rst)
app.include_router(router=router_v1, prefix=settings.api_v1_prefix)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {
        "message": f"Hello {name}!",
    }


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == "__main__":
    uvicorn.run("app:app", reload=True)
