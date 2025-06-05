from fastapi import APIRouter

router = APIRouter()

@router.get("/healthcheck", tags=["Health"])
async def healthcheck():
    return {"status": "ok"}
