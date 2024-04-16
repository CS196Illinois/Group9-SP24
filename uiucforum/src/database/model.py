import csv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf import FlaskForm



Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    username = Column('username', String(50), unique=True)

    def __init__(self, id, username):
        self.id = id
        self.username = username

    def __repr__(self):
        return f"{self.id} {self.username}"
    

class Post(Base):
    __tablename__ = 'posts'
    id = Column('posts_id', Integer, primary_key=True)
    title = Column('title', String(100))
    body = Column('body', Text)
    user_id = Column('user_id', Integer)

    def __init__(self, id, title, body, user_id):
        self.id = id
        self.title = title
        self.body = body
        self.user_id = user_id
    
    def __repr__(self):
        return f"{self.id} {self.title} {self.body} {self.user_id}"




class Comment(Base):
    __tablename__ = 'comments'
    id = Column('comments_id', Integer, primary_key=True)
    body = Column('body', Text)
    user_id = Column('users_id', Integer)

    def __init__(self, id, body, user_id):
        self.id = id
        self.body = body
        self.user_id = user_id
    
    def __repr__(self):
        return f"{self.id} {self.body} {self.user_id}"
    

