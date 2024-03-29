from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas, models
from psyncly.crud.resources_crud import ServicePlaylistCrud
from psyncly.dependencies import get_db
from psyncly.schemas.service_playlist_schemas import (
    ServicePlaylist,
    CreateServicePlaylist,
)

router = APIRouter(
    tags=["Service Playlists"],
    prefix="/users/{user_id}/service_playlists",
)


@router.get("", response_model=list[ServicePlaylist])
async def list_service_playlists(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return ServicePlaylistCrud(db).get(
        skip,
        limit,
        filters=(models.ServicePlaylist.owner_id == user_id,),
    )


@router.get("/{service_playlist_id}", response_model=ServicePlaylist)
async def get_service_playlist(
    user_id: int,
    service_playlist_id: int,
    db: Session = Depends(get_db),
):
    service_playlist = ServicePlaylistCrud(db).get_by_id(
        id=service_playlist_id,
        filters=(
            models.ServicePlaylist.id == service_playlist_id,
            models.ServicePlaylist.owner_id == user_id,
        ),
    )
    if not service_playlist:
        raise HTTPException(status_code=404)

    return service_playlist


@router.post("", response_model=ServicePlaylist, status_code=201)
async def create_service_playlist(
    user_id: int,
    service_playlist: CreateServicePlaylist,
    db: Session = Depends(get_db),
):
    service_playlist_dict = dict(service_playlist)
    service_playlist_dict.update(owner_id=user_id)

    return ServicePlaylistCrud(db).create(obj=service_playlist_dict)


# @router.put("/{service_playlist_id}")
# async def modify_service_playlist(db: Session = Depends(get_db)):
#     return "TODO"


@router.delete("/{service_playlist_id}", status_code=204)
async def delete_service_playlist(
    user_id: int, service_playlist_id: int, db: Session = Depends(get_db)
):
    ServicePlaylistCrud(db).delete_by_id(
        id=service_playlist_id,
        filters=(models.ServicePlaylist.owner_id == user_id,),
    )
