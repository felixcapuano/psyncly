from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import models
from psyncly.crud.resources_crud import ServiceAccountCrud
from psyncly.schemas.service_account_schemas import ServiceAccount, CreateServiceAccount
from psyncly.dependencies import get_db

router = APIRouter(
    tags=["Service Accounts"], prefix="/users/{user_id}/service_accounts"
)


@router.get("", response_model=list[ServiceAccount])
async def list_service_accounts(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return ServiceAccountCrud(db).get(
        skip,
        limit,
        filters=(models.Playlist.owner_id == user_id,),
    )


@router.get("/{service_account_id}", response_model=ServiceAccount)
async def get_service_account(
    user_id: int,
    service_account_id: int,
    db: Session = Depends(get_db),
):
    service_account = ServiceAccountCrud(db).get_by_id(
        id=service_account_id,
        filters=(models.Playlist.owner_id == user_id,),
    )
    if not service_account:
        raise HTTPException(status_code=404)

    return service_account


@router.post("", response_model=ServiceAccount, status_code=201)
async def create_service_account(
    user_id: int,
    service_account: CreateServiceAccount,
    db: Session = Depends(get_db),
):
    service_account_dict = dict(service_account)
    service_account_dict.update(owner_id=user_id)

    return ServiceAccountCrud(db).create(obj=service_account_dict)


# @router.put("/{service_playlist_id}")
# async def modify_service_account(db: Session = Depends(get_db)):
#     return "TODO"


@router.delete("/{service_account_id}")
async def delete_service_account(
    user_id: int,
    service_account_id: int,
    db: Session = Depends(get_db),
):
    ServiceAccountCrud(db).delete_by_id(
        id=service_account_id,
        filters=(models.Playlist.owner_id == user_id,),
    )
