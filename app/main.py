from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.products import router as products_router
from app.core.redis import redis_client


@asynccontextmanager
async def lifespan(app: FastAPI):
    await redis_client.ping()

    yield

    await redis_client.aclose()


app = FastAPI(
    title="Redis Backend Project",
    lifespan=lifespan,
)

app.include_router(products_router)