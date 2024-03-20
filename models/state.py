#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
            cascade="all, delete, delete-orphan")

<<<<<<< HEAD
=======
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ list down related cities"""
            store = models.storage.all(City).values()
            citys = [city for City in store if city.state_id == self.id]
            return citys
>>>>>>> 92e4348534ad1ec350d535da76d126ce213327c2
