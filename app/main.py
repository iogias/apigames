from typing import Dict

from fastapi import FastAPI

# from app.core.config import settings

# app = FastAPI(
#     debug=True,
#     title=settings.APP_NAME,
#     openapi_url=f"{settings.API_V1_STR}/openapi.json",  # noqa
# )

app = FastAPI()


@app.get("/")
def index() -> Dict:
    return {"message": "Hey You!"}
