from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import models
from psyncly.crud.resources_crud import WorkerCrud
from psyncly.dependencies import get_db
from psyncly.schemas.worker_schemas import Worker, CreateWorker

router = APIRouter(
    tags=["Workers"], prefix="/users/{user_id}/playlists/{playlist_id}/workers"
)


@router.get("", response_model=list[Worker])
async def list_workers(
    user_id: int,
    playlist_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return WorkerCrud(db).get(
        skip=skip,
        limit=limit,
        filters=(
            models.Worker.playlist_id == playlist_id,
            models.Worker.playlist.owner_id == user_id,
        ),
    )


@router.get("/{worker_id}", response_model=Worker)
async def get_worker(
    user_id: int,
    playlist_id: int,
    worker_id: int,
    db: Session = Depends(get_db),
):
    worker = WorkerCrud(db).get_by_id(
        id=worker_id,
        filters=(
            models.Worker.playlist_id == playlist_id,
            models.Worker.playlist.owner_id == user_id,
        ),
    )
    if not worker:
        raise HTTPException(status_code=404)

    return worker


@router.post("", response_model=Worker)
async def create_worker(
    playlist_id: int,
    worker: CreateWorker,
    db: Session = Depends(get_db),
):
    worker_dict = dict(worker)
    worker_dict.update(playlist_id=playlist_id)

    return WorkerCrud(db).create(obj=worker_dict)


# @router.put("/{service_playlist_id}")
# async def modify_worker(db: Session = Depends(get_db)):
#     return "TODO"


@router.delete("/{worker_id}", status_code=204)
async def delete_worker(
    user_id: int,
    playlist_id: int,
    worker_id: int,
    db: Session = Depends(get_db),
):
    WorkerCrud(db).delete_by_id(
        id=worker_id,
        filters=(
            models.Worker.playlist_id == playlist_id,
            models.Worker.playlist.owner_id == user_id,
        ),
    )
