from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas, models
from psyncly.crud.resources_crud import PlaylistCrud, TrackCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Playlists"], prefix="/playlists")


@router.get("", response_model=list[schemas.Playlist])
async def list_playlists(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return PlaylistCrud(db).get(None, skip, limit)


@router.get("/{playlist_id}", response_model=schemas.Playlist)
async def get_playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = PlaylistCrud(db).get_by_id(id=playlist_id)
    if not playlist:
        raise HTTPException(status_code=404)

    return playlist


@router.post("", status_code=201, response_model=schemas.Playlist)
async def create_playlist(
    playlist: schemas.CreatePlaylist, db: Session = Depends(get_db)
):
    return PlaylistCrud(db).create(obj=playlist)


@router.put("/{playlist_id}", response_model=schemas.Playlist)
async def modify_playlist(
    playlist_id: int, playlist: schemas.ModifyPlaylist, db: Session = Depends(get_db)
):
    return PlaylistCrud(db).modify(id=playlist_id, obj=playlist)


@router.delete("/{playlist_id}", status_code=204)
async def delete_playlist(playlist_id: int, db: Session = Depends(get_db)):
    PlaylistCrud(db).delete_by_id(id=playlist_id)


@router.get(
    "/{playlist_id}/tracks",
    # response_model=list[schemas.Track],
)
async def list_playlist_tracks(playlist_id: int, db: Session = Depends(get_db)):
    return PlaylistCrud(db).get_by_id(id=playlist_id).tracks


@router.patch("/{playlist_id}/tracks", status_code=204)
async def update_playlist_tracks(
    playlist_id: int, operations: list[schemas.Operation], db: Session = Depends(get_db)
):
    for op in operations:
        playlist = PlaylistCrud(db).get_by_id(id=playlist_id)
        track = TrackCrud(db).get_by_id(id=op.resource_id)

        if op.type == "add":
            playlist.tracks.append(track)
        elif op.type == "remove":
            playlist.tracks.remove(track)

    db.commit()
