# backend/app/api/api_v1/api.py

from fastapi import APIRouter
from app.api.api_v1.endpoints import auth, users, profiles, matching, messages, recommendations

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(profiles.router, prefix="/profiles", tags=["profiles"])
api_router.include_router(matching.router, prefix="/matching", tags=["matching"])
api_router.include_router(messages.router, prefix="/messages", tags=["messages"])
api_router.include_router(recommendations.router, prefix="/recommendations", tags=["recommendations"])
