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
from sqlalchemy.orm import sessionmaker, scoped_session

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
        
    def all(self, cls=None):
        """
        returns a dictionary of objects in the databse
        """
        dictionary = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dictionary[key] = elem
        lista = [State ,City, User, Place, Review, Amenity]
        for clas in lista:
            query = self.__session.query(clas)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dictionary[key] = elem
            return dictionary
        
    def new(self, obj):
        """add a new element in the table
        """
        self.__session.add(obj)

    def save(self):
        """save changes
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.session.delete(obj)

    def reload(self):
        """
        creates the database
        """
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """
        closes the current session
        """
        self.__session.close()


        



