from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas
from psyncly.crud.resources_crud import PlaylistCrud, PlaylistTrackRelationCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Playlists"], prefix="/playlists")


@router.get("", response_model=list[schemas.ReadPlaylist])
async def list_playlists(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return PlaylistCrud(db).get(None, skip, limit)


@router.get("/{playlist_id}", response_model=schemas.ReadPlaylist)
async def get_playlist(playlist_id: int, db: Session = Depends(get_db)):
    playlist = PlaylistCrud(db).get_by_id(id=playlist_id)
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
async def list_playlist(
    playlist_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return PlaylistTrackRelationCrud(db).get(None, skip, limit)


@router.patch("/{playlist_id}/tracks", status_code=204)
async def update_playlist(
    playlist_id: int, operations: list[schemas.Operation], db: Session = Depends(get_db)
):
    for op in operations:
        if op.type == "add":
            new_relation = schemas.WritePlaylistTrackRelation(
                playlist_id=playlist_id,
                track_id=op.resource_id,
            )
            PlaylistTrackRelationCrud(db).create(new_relation)
        elif op.type == "remove":
            pass
            # PlaylistTrackRelationCrud(db).list(playlist_id)
            # PlaylistTrackRelationCrud(db).delete({"playlist_id": playlist_id, "track_id": op.resource_id})
        else:
            raise HTTPException(status_code=400, detail="Unkown operation")
