from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import models
from psyncly.crud.resources_crud import AccountCrud
from psyncly.schemas.account_schemas import Account, CreateAccount
from psyncly.dependencies import get_db

router = APIRouter(
    tags=["Service Accounts"],
    prefix="/users/{user_id}/accounts",
)


@router.get("", response_model=list[Account])
async def list_accounts(
    user_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
):
    return AccountCrud(db).get(
        skip,
        limit,
        filters=(models.Playlist.owner_id == user_id,),
    )


@router.get("/{account_id}", response_model=Account)
async def get_account(
    user_id: int,
    account_id: int,
    db: Session = Depends(get_db),
):
    account = AccountCrud(db).get_by_id(
        id=account_id,
        filters=(models.Playlist.owner_id == user_id,),
    )
    if not account:
        raise HTTPException(status_code=404)

    return account


@router.post("", response_model=Account, status_code=201)
async def create_account(
    user_id: int,
    account: CreateAccount,
    db: Session = Depends(get_db),
):
    account_dict = dict(account)
    account_dict.update(owner_id=user_id)

    return AccountCrud(db).create(obj=account_dict)


# @router.put("/{service_playlist_id}")
# async def modify_account(db: Session = Depends(get_db)):
#     return "TODO"


@router.delete("/{account_id}")
async def delete_account(
    user_id: int,
    account_id: int,
    db: Session = Depends(get_db),
):
    AccountCrud(db).delete_by_id(
        id=account_id,
        filters=(models.Playlist.owner_id == user_id,),
    )
