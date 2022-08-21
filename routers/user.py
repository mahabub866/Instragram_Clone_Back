from enum import Enum
from fastapi import APIRouter, status, Response, Query, Body, Path,Depends
from typing import Dict, List, Optional, Union

from sqlalchemy.orm.session import Session
from db.database import get_db
from repository.db_user import create_user

from routers.schemas import UserBase, UserDisplay

router=APIRouter(
    prefix='/user',
    tags=['User']
)

# create
@router.post('/create',response_model=UserDisplay)
def create_users(request:UserBase,db:Session=Depends(get_db)):
    return create_user(db,request)
