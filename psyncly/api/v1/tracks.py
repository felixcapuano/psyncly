from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas
from psyncly.crud.resources_crud import TrackCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Tracks"], prefix="/tracks")


@router.get("", response_model=list[schemas.ReadTrack])
async def list_tracks(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return TrackCrud(db).get(None, skip, limit)


@router.get("/{track_id}", response_model=schemas.ReadTrack)
async def get_track(track_id: int, db: Session = Depends(get_db)):
    track = TrackCrud(db).get_by_id(id=track_id)
    if not track:
        raise HTTPException(status_code=404)

    return track


@router.post("", status_code=201, response_model=schemas.ReadTrack)
async def create_track(track: schemas.WriteTrack, db: Session = Depends(get_db)):
    return TrackCrud(db).create(obj=track)


@router.put("/{track_id}", response_model=schemas.ReadTrack)
async def modify_track(
    track_id: int, track: schemas.WriteTrack, db: Session = Depends(get_db)
):
    return TrackCrud(db).modify(id=track_id, obj=track)


@router.delete("/{track_id}", status_code=204)
async def delete_track(track_id: int, db: Session = Depends(get_db)):
    TrackCrud(db).delete_by_id(id=track_id)
