from sqlalchemy.orm.session import Session
from routers.schemas import UserBase
from db.models import DbUser
from db.hasing import Hash
from fastapi import HTTPException,status

def create_user(db:Session,request:UserBase):
    new_user = DbUser(username=request.username,
                      email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user