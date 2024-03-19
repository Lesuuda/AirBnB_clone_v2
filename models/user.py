#!/usr/bin/python3

from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel

Base = declarative_base()
"""
A class that defines a USEr
"""
class User(BaseModel, Base):
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

