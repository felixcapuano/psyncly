from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas, models
from psyncly.crud.resources_crud import ServicePlaylistCrud
from psyncly.dependencies import get_db
from psyncly.schemas.service_playlist_schemas import ServicePlaylist

router = APIRouter(
    tags=["Service Playlists"],
    prefix="/users/{user_id}/playlists/{playlist_id}/service_playlists",
)


@router.get("", response_model=list[ServicePlaylist])
async def list_service_playlists(
    user_id: int,
    playlist_id: int,
    skip: int = 0,
    limit: int = 0,
    db: Session = Depends(get_db),
):
    return ServicePlaylistCrud(db).get(
        skip, limit, filters={"playlist_id": playlist_id}
    )


@router.get("/{service_playlist_id}", response_model=ServicePlaylist)
async def get_service_playlist(
    user_id: int,
    playlist_id: int,
    service_playlist_id: int,
    db: Session = Depends(get_db),
):
    service_playlist = ServicePlaylistCrud(db).get_by_id(
        id=service_playlist_id, filters={"playlist_id": playlist_id}
    )
    if not service_playlist:
        raise HTTPException(status_code=404)

    return service_playlist


@router.post("", response_model=ServicePlaylist, status_code=201)
async def create_service_playlist(
    user_id: int,
    playlist_id: int,
    db: Session = Depends(get_db),
):
    return "TODO"


# @router.put("/{service_playlist_id}")
# async def modify_service_playlist(db: Session = Depends(get_db)):
#     return "TODO"


@router.delete("/{service_playlist_id}")
async def delete_service_playlist(db: Session = Depends(get_db)):
    return "TODO"
