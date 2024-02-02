from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas, models
from psyncly.crud.resources_crud import PlaylistCrud, TrackCrud
from psyncly.dependencies import get_db

router = APIRouter(
    tags=["Service Accounts"], prefix="/users/{user_id}/service_accounts"
)


@router.get("")
async def list_service_accounts(db: Session = Depends(get_db)):
    return "TODO"


@router.post("")
async def create_service_account(db: Session = Depends(get_db)):
    return "TODO"


@router.get("/{service_playlist_id}")
async def get_service_account(db: Session = Depends(get_db)):
    return "TODO"


@router.delete("/{service_playlist_id}")
async def delete_service_account(db: Session = Depends(get_db)):
    return "TODO"


@router.put("/{service_playlist_id}")
async def modify_service_account(db: Session = Depends(get_db)):
    return "TODO"
