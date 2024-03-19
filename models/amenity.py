#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represents the Amenity in sql"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
