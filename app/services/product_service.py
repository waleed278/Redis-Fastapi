import asyncio
import json

from app.core.config import settings
from app.core.redis import redis_client


PRODUCTS = {
    1: {
        "id": 1,
        "name": "Mechanical Keyboard",
        "price": 12000,
    },
    2: {
        "id": 2,
        "name": "Wireless Mouse",
        "price": 4500,
    },
}


async def get_product_from_source(product_id: int):
    await asyncio.sleep(1)

    return PRODUCTS.get(product_id)


async def get_product(product_id: int):
    cache_key = f"product:{product_id}"

    cached_product = await redis_client.get(cache_key)

    if cached_product is not None:
        return {
            "source": "cache",
            "product": json.loads(cached_product),
        }

    product = await get_product_from_source(product_id)

    if product is None:
        return None

    await redis_client.set(
        cache_key,
        json.dumps(product),
        ex=settings.cache_ttl_seconds,
    )

    return {
        "source": "source",
        "product": product,
    }