from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly import schemas
from psyncly.crud.resources_crud import UserCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("", response_model=list[schemas.ReadUser])
async def list_user(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return UserCrud(db).get(None, skip, limit)


@router.get("/{user_id}", response_model=schemas.ReadUser)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserCrud(db).get_by_id(id=user_id)
    if not user:
        raise HTTPException(status_code=404)

    return user


@router.post("", status_code=201, response_model=schemas.ReadUser)
async def create_user(user: schemas.WriteUser, db: Session = Depends(get_db)):
    return UserCrud(db).create(obj=user)


@router.put("/{user_id}", response_model=schemas.ReadUser)
async def modify_user(
    user_id: int, user: schemas.WriteUser, db: Session = Depends(get_db)
):
    return UserCrud(db).modify(id=user_id, obj=user)


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserCrud(db).delete_by_id(id=user_id)
