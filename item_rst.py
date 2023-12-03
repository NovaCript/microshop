from typing import Annotated
from fastapi import Path, APIRouter

items_rst = APIRouter(prefix="/items", tags=["Items"])


@items_rst.get("/")
def list_items():
    return [
        "Item1",
        "Item2",
        "Item3",
    ]


@items_rst.get("/latest/")
def get_latest_item():
    return {"item": {"id": "0", "name": "latest"}}


@items_rst.get("/{item_id}/")
def get_item_by_id(item_id: Annotated[int, Path(ge=1, lt=1_000_000)]):
    return {
        "item": {
            "id": item_id,
        },
    }
