#!/usr/bin/python3
""" holds class party"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class Party(BaseModel, Base):
    """Representation for party """
    if models.storage_t == 'db':
        __tablename__ = 'party'
        id = Column(Integer(11), nullable=False, autoincrement=True, primary_key=True)
        partyid = Column(String(11), nullable=False)
        partyname = Column(String(11), nullable=False)

    else:
        result_id = 0
        partyid = ""
        partyname = ""

    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
