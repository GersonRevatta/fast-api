from fastapi import FastAPI
from app.api.v1.endpoints import user
from app.core.config import settings

app = FastAPI(title="My Project API", version="v1")

app.include_router(user.router, prefix="/api/v1/users", tags=["Users"])
