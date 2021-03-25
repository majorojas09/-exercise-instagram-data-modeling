import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Login(Base):
    __tablename__ = 'login'
    username = Column(String(250), primary_key=True)
    password = Column(String(250), nullable=False)
    
class Register(Base):
    __tablename__ = 'userRegister'
    userId = Column(Integer, primary_key=True)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    username_User = Column(String(250), ForeignKey('login.username'))
    password_User = Column(String(250), nullable=False)
    login = relationship(Login)

class Post(Base):
    __tablename__ = 'post'
    postId = Column(Integer, primary_key=True)
    postDesc = Column(String(250), nullable=True)
    likesPost = Column(Integer, nullable=False)
    userId_User = Column(Integer, ForeignKey('userRegister.userId'))
    userRegister = relationship(Register)

class Comment(Base):
    __tablename__ = 'comment'
    commentId = Column(Integer, primary_key=True)
    commentDesc = Column(String(250), nullable=True)
    userId_us = Column(Integer, ForeignKey('userRegister.userId'))
    postId_post = Column(Integer, ForeignKey('post.postId'))
    userRegister = relationship(Register)
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')