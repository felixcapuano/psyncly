from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from psyncly.schemas import user_schemas
from psyncly.crud.resources_crud import UserCrud
from psyncly.dependencies import get_db

router = APIRouter(tags=["Users"], prefix="/users")


@router.get("", response_model=list[user_schemas.User])
async def list_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return UserCrud(db).get(skip, limit)


@router.get("/{user_id}", response_model=user_schemas.User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = UserCrud(db).get_by_id(id=user_id)
    if not user:
        raise HTTPException(status_code=404)

    return user


@router.post("", status_code=201, response_model=user_schemas.User)
async def create_user(user: user_schemas.CreateUser, db: Session = Depends(get_db)):
    return UserCrud(db).create(obj=user)


# @router.put("/{user_id}", response_model=user_schemas.User)
# async def modify_user(
#     user_id: int, user: user_schemas.ModifyUser, db: Session = Depends(get_db)
# ):
#     return UserCrud(db).modify(id=user_id, obj=user)


@router.delete("/{user_id}", status_code=204)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    UserCrud(db).delete_by_id(id=user_id)
