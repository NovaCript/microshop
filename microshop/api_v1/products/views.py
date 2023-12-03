from fastapi import APIRouter, HTTPException, status, Depends
from microshop.core.models import db_helper
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from .dependencies import product_by_id
from .shenas import Product, ProductCreate, ProductUpdate, ProductUpdatePartial

product_rst = APIRouter(tags=["Products"])


@product_rst.get("/", response_model=list[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.scoped_session_dependensy),
):
    return await crud.get_products(session=session)


@product_rst.post("/", response_model=Product, status_code=status.HTTP_201_CREATED)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependensy),
):
    return await crud.create_product(session=session, product_in=product_in)


@product_rst.get("/{product_id}/", response_model=Product)
async def get_product(
    product: Product = Depends(product_by_id),
):
    return product


@product_rst.put("/{product_id}/")
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependensy),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


@product_rst.patch("/{product_id}/")
async def update_product_partial(
    product_update: ProductUpdatePartial,
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependensy),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
        partial=True,
    )


@product_rst.delete("/{product_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    product: Product = Depends(product_by_id),
    session: AsyncSession = Depends(db_helper.scoped_session_dependensy),
)->None:
    await crud.delete_product(session=session, product=product)