from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from psyncly.schemas import playlist_schemas, track_schemas, common_schemas
from psyncly.crud.resources_crud import PlaylistCrud, TrackCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Playlists"], prefix="/users/{user_id}/playlists")


@router.get("", response_model=list[playlist_schemas.Playlist])
async def list_playlists(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return PlaylistCrud(db).get(skip, limit, filters={"owner_id": user_id})


@router.get("/{playlist_id}", response_model=playlist_schemas.Playlist)
async def get_playlist(
    user_id: int,
    playlist_id: int,
    db: Session = Depends(get_db),
):
    playlist = PlaylistCrud(db).get_by_id(id=playlist_id, filters={"owner_id": user_id})
    if not playlist:
        raise HTTPException(status_code=404)

    return playlist


@router.post("", status_code=201, response_model=playlist_schemas.Playlist)
async def create_playlist(
    user_id: int,
    playlist: playlist_schemas.CreatePlaylist,
    db: Session = Depends(get_db),
):
    playlist_dict = dict(playlist)
    playlist_dict.update(owner_id=user_id)

    return PlaylistCrud(db).create(obj=playlist_dict)


# @router.put("/{playlist_id}", response_model=playlist_schemas.Playlist)
# async def modify_playlist(
#     user_id: int,
#     playlist_id: int,
#     playlist: playlist_schemas.ModifyPlaylist,
#     db: Session = Depends(get_db),
# ):

#     return PlaylistCrud(db).modify(id=playlist_id, obj=playlist)


@router.delete("/{playlist_id}", status_code=204)
async def delete_playlist(
    user_id: int,
    playlist_id: int,
    db: Session = Depends(get_db),
):
    PlaylistCrud(db).delete_by_id(id=playlist_id)


@router.get("/{playlist_id}/tracks", response_model=list[track_schemas.Track])
async def list_playlist_tracks(
    user_id: int,
    playlist_id: int,
    db: Session = Depends(get_db),
):
    return PlaylistCrud(db).get_by_id(id=playlist_id).tracks


@router.patch("/{playlist_id}/tracks", status_code=204)
async def update_playlist_tracks(
    user_id: int,
    playlist_id: int,
    operations: list[common_schemas.Operation],
    db: Session = Depends(get_db),
):
    for op in operations:
        playlist = PlaylistCrud(db).get_by_id(id=playlist_id)
        track = TrackCrud(db).get_by_id(id=op.resource_id)

        if op.type == "add":
            playlist.tracks.append(track)
        elif op.type == "remove":
            playlist.tracks.remove(track)

    db.commit()
