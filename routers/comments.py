from fastapi import APIRouter,HTTPException,status,Depends
from db.database import get_db
from repository.db_comments import create, get_all
from routers.schemas import PostDisplay, UserAuth,CommentBase

from sqlalchemy.orm.session import Session
from auth.oauth2 import get_current_user
router=APIRouter(
    prefix='/comment',
    tags=['Comment']
)

@router.post('/create')
def create_comment(request: CommentBase, db: Session = Depends(get_db),current_user:UserAuth=Depends(get_current_user)):
    # if not request.image_url_type in image_url_types:
    #     raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
    #                         detail="Parameter image_url_type can only take values 'absolute' or 'relative'  ")
    return create(db, request)

@router.get('/all/{post_id}')
def get_all_comment(post_id:int,db:Session=Depends(get_db)):
    return get_all(db,post_id)
