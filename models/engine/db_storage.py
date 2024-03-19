#!/usr/bin/python3
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import json
from os import getenv
from sqlalchemy import create_engine

"""This module defines a class to manage database storage for hbnb clone"""

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user  = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        database = getenv("HBNB_MYSQL_DB")
        env = getenv("HBNB_ENV")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host, database, pool_pre_ping=True))

        if env == 'test':
            Base.metadata.drop_all(self.__engine)
