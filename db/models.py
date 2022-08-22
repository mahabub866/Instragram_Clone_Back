
from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from sqlalchemy.orm import relationship


class DbUser(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String)
    email=Column(String)
    password=Column(String)
    # user_id=Column(Integer,ForeignKey('users.id'))
    items= relationship("DbPost", back_populates="user")

class DbPost(Base):
    __tablename__='posts'
    id=Column(Integer,primary_key=True,index=True)
    image_url=Column(String)
    image_url_type=Column(String)
    caption=Column(String)
    timestamp=Column(DateTime)
    user_id=Column(Integer,ForeignKey('users.id'))
    user= relationship("DbUser", back_populates="items")
    comments= relationship("DbComment", back_populates="post")
    

class DbComment(Base):
    __tablename__='comments'
    id=Column(Integer,primary_key=True,index=True)
    text=Column(String)
    username=Column(String)
    timestamp=Column(DateTime)
    post_id=Column(Integer,ForeignKey('posts.id'))
    post= relationship("DbPost", back_populates="comments")
