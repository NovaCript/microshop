from fastapi import APIRouter

from .products.views import product_rst


router = APIRouter()
router.include_router(router=product_rst, prefix="/products")
