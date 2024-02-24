#!/usr/bin/python3
""" holds class ward"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from hashlib import md5


class Ward(BaseModel, Base):
    """Represen ward"""
    if models.storage_t == 'db':
        __tablename__ = 'ward'
        uniqueid = Column(Integer(), nullable=False, autoincrement=True, primary_key=True)
        ward_id = Column(Integer(), nullable=False)
        ward_name = Column(String(50), nullable=False)
        lga_id = Column(Integer(), nullable=False)
        ward_description = Column(String, nullable=False)
        entered_by_user = Column(String(50), nullable=False)
        date_entered = Column(DateTime, nullable=False)
        user_ip_address = Column(String(50), nullable=False)

    else:
        uniqueid = 0
        ward_id = 0
        ward_name = ""
        lga_id = 0
        ward_description = ""
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
