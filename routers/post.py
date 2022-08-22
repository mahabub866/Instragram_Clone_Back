from enum import Enum

from fastapi import APIRouter, status, Response, Query, Body, Path, UploadFile,File,Depends, status,HTTPException
from typing import Dict, List, Optional, Union
import string
from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
from db.database import get_db
from repository.db_post import create, delete_post, get_all
import shutil
import random
from routers.schemas import PostBase, PostDisplay, UserBase, UserDisplay,UserAuth

router = APIRouter(
    prefix='/post',
    tags=['Post']
)

image_url_types = ['absolute', 'relative']
# create


@router.post('/create', response_model=PostDisplay)
def create_post(request: PostBase, db: Session = Depends(get_db),current_user:UserAuth=Depends(get_current_user)):
    if not request.image_url_type in image_url_types:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Parameter image_url_type can only take values 'absolute' or 'relative'  ")
    return create(db, request)

@router.get('/all',response_model=List[PostDisplay])
def get_all_post(db:Session=Depends(get_db)):
    return get_all(db)

# image part
@router.post('/image')
def upload_image(image:UploadFile=File(...),current_user:UserAuth=Depends(get_current_user)):
    letter=string.ascii_letters
    rand_str=''.join(random.choice(letter) for i in range(6))
    new =f'_{rand_str}.'
    filename=new.join(image.filename.rsplit('.',1))
    path = f'images/{filename}'
    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {'filename': path}

@router.get('/delete/{id}')
def delete(id:int,db:Session=Depends(get_db),current_user:UserAuth=Depends(get_current_user)):
    print(current_user)
    owner_id=current_user.id

    return delete_post(db,id,owner_id)