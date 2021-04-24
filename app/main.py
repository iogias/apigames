from typing import Dict

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.core.config import settings

app = FastAPI(
    debug=True,
    title=settings.APP_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",  # noqa
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],  # noqa
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/")
def index() -> Dict:
    return {"message": "Hey You!"}
