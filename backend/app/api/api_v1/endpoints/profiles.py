from fastapi import APIRouter

router = APIRouter()

@router.get("/test-profiles")
async def test_route():
    return {"message": "profiles router 연결 성공!"}
