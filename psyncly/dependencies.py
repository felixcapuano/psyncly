from fastapi import Depends, HTTPException
from psyncly.database import SessionLocal
from psyncly.crud.resources_crud import UserCrud, PlaylistCrud, AccountCrud
from sqlalchemy.orm import Session


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_user(user_id: int, db: Session = Depends(get_db)):
    return UserCrud(db).get_by_id(id=user_id)


def playlist_belong_to_user(
    user_id: int, playlist_id: int, db: Session = Depends(get_db)
):
    playlist = PlaylistCrud(db).get_by_id(id=playlist_id)

    if playlist.owner_id != user_id:
        raise HTTPException(status_code=404)

    return True


def account_belong_to_user(
    user_id: int, account_id: int, db: Session = Depends(get_db)
):
    account = AccountCrud(db).get_by_id(id=account_id)

    if account.owner_id != user_id:
        raise HTTPException(status_code=404)

    return True
