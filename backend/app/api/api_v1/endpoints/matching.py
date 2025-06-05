from fastapi import APIRouter

router = APIRouter()

@router.get("/test-matching")
async def test_route():
    return {"message": "matching router 연결 성공!"}
