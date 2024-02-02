from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas, models
from psyncly.crud.resources_crud import PlaylistCrud, TrackCrud
from psyncly.dependencies import get_db

router = APIRouter(
    tags=["Service Playlists"],
    prefix="/users/{user_id}/playlists/{playlist_id}/service_playlists",
)


@router.get("")
async def list_service_playlists(db: Session = Depends(get_db)):
    return "TODO"


@router.post("")
async def create_service_playlist(db: Session = Depends(get_db)):
    return "TODO"


@router.get("/{service_playlist_id}")
async def get_service_playlist(db: Session = Depends(get_db)):
    return "TODO"


@router.delete("/{service_playlist_id}")
async def delete_service_playlist(db: Session = Depends(get_db)):
    return "TODO"


@router.put("/{service_playlist_id}")
async def modify_service_playlist(db: Session = Depends(get_db)):
    return "TODO"
