from app.services.product_service import get_product
from fastapi import HTTPException,status, APIRouter
router = APIRouter(
    prefix="/products",
    tags= ["products"],
)

@router.get("/{product_id}")
async def read_product(product_id:int):
    result = await get_product(product_id)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No product exists"
        )
    return result