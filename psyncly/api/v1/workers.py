from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas, models
from psyncly.crud.resources_crud import PlaylistCrud, TrackCrud
from psyncly.dependencies import get_db

router = APIRouter(
    tags=["Workers"], prefix="/users/{user_id}/playlists/{playlist_id}/workers"
)


@router.get("")
async def list_workers(db: Session = Depends(get_db)):
    return "TODO"


@router.post("")
async def create_worker(db: Session = Depends(get_db)):
    return "TODO"


@router.get("/{service_playlist_id}")
async def get_worker(db: Session = Depends(get_db)):
    return "TODO"


@router.delete("/{service_playlist_id}")
async def delete_worker(db: Session = Depends(get_db)):
    return "TODO"


@router.put("/{service_playlist_id}")
async def modify_worker(db: Session = Depends(get_db)):
    return "TODO"
