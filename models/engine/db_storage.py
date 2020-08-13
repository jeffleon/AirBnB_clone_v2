#!/usr/bin/python3
"""
Class of the database storage
"""

import sqlalchemy
import os
from sqlalchemy import create_engine
from sys import argv
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}


class DBStorage:
    __engine = None
    __session = None
    environment = os.getenv("HBNB_ENV")
    def __init__(self):
        """Init method"""
        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.\
                                      format(user, passwd, host, db),\
                                      pool_pre_ping=True)
        if self.environment == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query in the current database"""
        session = self.__session
        dictionary = {}
        if (not cls):
            hbn = classes
        else:
            if (type(cls) == str):
                cls = eval(cls)
            hbn = [cls]
        for x in hbn:
            sql = session.query(x)
            for i in sql:
                key = "{}.{}".format(type(i).__name__, i.id)
                dictionary[key] = i
        return (dictionary)

    def new(self, obj):
        """Add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all the changes of the current database session"""
        self.__session.commit()

    def delete(self, obj):
        """Delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reload the data"""
        Base.metadata.create_all(self.__engine)
        cur_sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session2 = scoped_session(cur_sess)
        self.__session = session2
