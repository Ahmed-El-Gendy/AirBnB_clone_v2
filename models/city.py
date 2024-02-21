#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = column(string(60), nullable=False, foreignkey('states.id'))
    name = column(string(128), nullable=False)
