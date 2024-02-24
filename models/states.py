#!/usr/bin/python3
""" holds class states"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class States(BaseModel, Base):
    """Representation for states """
    if models.storage_t == 'db':
        __tablename__ = 'states'
        state_id = Column(Integer(11), nullable=False, primary_key=True)
        state_name = Column(String(50), nullable=False)

    else:
        state_id = 0
        state_name = ""

    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
