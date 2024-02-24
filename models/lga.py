#!/usr/bin/python3
""" holds class lga"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class Lga(BaseModel, Base):
    """Representation for lga """
    if models.storage_t == 'db':
        __tablename__ = 'lga'
        uniqueid = Column(Integer(11), nullable=False, autoincrement=True, primary_key=True)
        lga_id = Column(Integer(11), nullable=False)
        lga_name = Column(String(50), nullable=False)
        state_id = Column(Integer(50), nullable=False)
        lga_description = Column(String, nullable=False)
        entered_by_user = Column(String(50), nullable=False)
        date_entered = Column(DateTime, nullable=False)
        user_ip_address = Column(String(50), nullable=False)

    else:
        uniqueid = 0
        lga_id = 0
        lga_name = ""
        lga_description = ""
        state_id = ""
        entered_by_user = ""
        date_entered = ""
        user_ip_address = ""

    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
