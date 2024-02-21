#!/usr/bin/python3
""" import models """

from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

class DBStorage:
    """ db class """
    __engine = None
    __session =  None
    def __init__(self):
        self.engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")),  pool_pre_ping=True)
        if (HBNB_ENV == test):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ new method """

