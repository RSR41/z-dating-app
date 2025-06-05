# backend/app/api/api_v1/endpoints/users.py

from fastapi import APIRouter

router = APIRouter()

@router.get("/test-users")
async def test_users():
    return {"message": "Users router 연결 성공!"}
