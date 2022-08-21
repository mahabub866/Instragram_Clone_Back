from enum import Enum
from fastapi.exceptions import HTTPException
from fastapi import APIRouter, status, Response, Query, Body, Path, Depends, status
from typing import Dict, List, Optional, Union

from sqlalchemy.orm.session import Session
from db.database import get_db
from repository.db_post import create

from routers.schemas import PostBase, PostDisplay, UserBase, UserDisplay

router = APIRouter(
    prefix='/post',
    tags=['Post']
)

image_url_types = ['absolute', 'relative']
# create


@router.post('/create', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            details="Parameter image_url_type can only take values 'absolute' or 'relative'  ")
    return create(db, request)
