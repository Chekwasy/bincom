#!/usr/bin/python3
"""
Contains the class DBStorage
"""
import uuid
import models
from models.agentname import Agentname
from models.announced_ward_results import Announced_ward_results
from models.lga import Lga
from models.party import Party
from models.polling_unit import Polling_unit
from models.states import States
from models.ward import Ward
from models.base_model import BaseModel, Base
from models.announced_lga_results import Announced_lga_results
from models.announced_pu_results import Announced_pu_results
from models.announced_state_results import Announced_state_results
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Agentname": Agentname, "BaseModel": BaseModel, "Announced_ward_results": Announced_ward_results, "Lga": Lga, "Party": Party, "Polling_unit": Polling_unit, "States": States, "Ward": Ward, "Announced_lga_results": Announced_lga_results, "Announced_pu_results": Announced_pu_results, "Announced_state_results": Announced_state_results}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        CHEKWASY_MYSQL_USER = getenv('CHEKWASY_MYSQL_USER')
        CHEKWASY_MYSQL_PWD = getenv('CHEKWASY_MYSQL_PWD')
        CHEKWASY_MYSQL_HOST = getenv('CHEKWASY_MYSQL_HOST')
        CHEKWASY_MYSQL_DB = getenv('CHEKWASY_MYSQL_DB')
        CHEKWASY_ENV = getenv('CHEKWASY_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(CHEKWASY_MYSQL_USER,
                                             CHEKWASY_MYSQL_PWD,
                                             CHEKWASY_MYSQL_HOST,
                                             CHEKWASY_MYSQL_DB))
        if CHEKWASY_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(uuid.uuid4())
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
