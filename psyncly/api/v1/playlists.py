from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas
from psyncly.crud.resources_crud import PlaylistCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Playlists"], prefix="/playlists")


@router.get("", response_model=list[schemas.ReadPlaylist])
async def list_playlists(
    db: Session = Depends(get_db), skip: int = 0, limit: int = 100
):
    return PlaylistCrud(db).list(skip, limit, {})


@router.get("/{playlist_id}", response_model=schemas.ReadPlaylist)
async def get_playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = PlaylistCrud(db).get(id=playlist_id)
    if not playlist:
        raise HTTPException(status_code=404)

    return playlist


@router.post("", status_code=201, response_model=schemas.ReadPlaylist)
async def create_playlist(
    playlist: schemas.WritePlaylist, db: Session = Depends(get_db)
):
    return PlaylistCrud(db).create(obj=playlist)


@router.put("/{playlist_id}", response_model=schemas.ReadPlaylist)
async def modify_playlist(
    playlist_id: int, playlist: schemas.WritePlaylist, db: Session = Depends(get_db)
):
    return PlaylistCrud(db).modify(id=playlist_id, obj=playlist)


@router.delete("/{playlist_id}", status_code=204)
async def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    PlaylistCrud(db).delete(id=playlist_id)


@router.get("/{playlist_id}/tracks", response_model=list[schemas.ReadTrack])
async def list_playlist(playlist_id: int, db: Session = Depends(get_db)):
    return []


@router.patch("/{playlist_id}/tracks", response_model=schemas.BulkOperation)
async def update_playlist(playlist_id: int, db: Session = Depends(get_db)):
    return True
