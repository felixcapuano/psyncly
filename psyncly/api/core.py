from fastapi import APIRouter

router = APIRouter(tags=["Core"])


@router.get("/ping")
async def ping():
    return "pong"


@router.get("/status")
async def status():
    return True
