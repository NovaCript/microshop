from fastapi import FastAPI
from microshop.views import users
from item_rst import items

import uvicorn

app = FastAPI()

app.include_router(items)
app.include_router(users)


@app.get("/")
def hello_index():
    return {
        "message": "Hello index!",
    }


@app.get("/hello/")
def hello(name: str = "World"):
    name = name.strip().title()
    return {"message": f"Hello {name}!"}


@app.get("/calc/add/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b,
    }


if __name__ == '__main__':
    uvicorn.run("app:app", reload=True)
