#!/usr/bin/python3
""" holds class agentname"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from hashlib import md5


class Agentname(BaseModel, Base):
    """Representation for agentname """
    if models.storage_t == 'db':
        __tablename__ = 'agentname'
        name_id = Column(Integer(), nullable=False, autoincrement=True, primary_key=True)
        first_name = Column(String(255), nullable=False)
        last_name = Column(String(255), nullable=False)
        email = Column(String(255), nullable=True)
        phone = Column(String(13), nullable=False)
        pollingunit_uniqueid = Column(Integer(), nullable=False)

    else:
        name_id = 0
        email = ""
        first_name = ""
        last_name = ""
        phone = ""
        pollingunit_uniqueid = 0

    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
