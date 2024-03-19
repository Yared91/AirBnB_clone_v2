#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

created_table = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("place_id"),
            primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenity_id"),
            primary_key=True, nullable=False)
        )

class Place(BaseModel, Base):
    """ Represents a place for sql """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
            viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Get all list of linked Reviews"""
            store = models.storage.all(Review).values()
            return [review for review in store if review.place_id == self.id]

        @property
        def amenities(self):
            """Sets linked amenities"""
            store = models.storage.all(Amenity).values()
            idamenity = self.amenity_ids
            return [amenity for amenity in store if amenity.id in idamenity]

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
