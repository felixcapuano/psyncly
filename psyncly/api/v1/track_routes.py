from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly.schemas import track_schemas
from psyncly.crud.resources_crud import TrackCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Tracks"], prefix="/tracks")


@router.get("", response_model=list[track_schemas.Track])
async def list_tracks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return TrackCrud(db).get(skip, limit)


@router.get("/{track_id}", response_model=track_schemas.Track)
async def get_track(track_id: int, db: Session = Depends(get_db)):
    track = TrackCrud(db).get_by_id(id=track_id)
    if not track:
        raise HTTPException(status_code=404)

    return track


@router.post("", status_code=201, response_model=track_schemas.Track)
async def create_track(track: track_schemas.CreateTrack, db: Session = Depends(get_db)):
    return TrackCrud(db).create(obj=dict(track))


# @router.put("/{track_id}", response_model=track_schemas.Track)
# async def modify_track(
#     track_id: int, track: track_schemas.ModifyTrack, db: Session = Depends(get_db)
# ):
#     return TrackCrud(db).modify(id=track_id, obj=track)


@router.delete("/{track_id}", status_code=204)
async def delete_track(track_id: int, db: Session = Depends(get_db)):
    TrackCrud(db).delete_by_id(id=track_id)
