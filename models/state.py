#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
import models
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref=backref(
            "state",
            cascade="all, delete, delete-orphan"
        )
    )

    @property
    def cities(self):
        var = models.storage.all()
        list1 = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                list1.append(var[key])
        for element in list1:
            if element.state_id == self.id:
                result.append(element)
        return (element)
