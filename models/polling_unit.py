#!/usr/bin/python3
""" holds class polling_unit"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from hashlib import md5


class Polling_unit(BaseModel, Base):
    """Representation for polling_unit """
    if models.storage_t == 'db':
        __tablename__ = 'polling_unit'
        uniqueid = Column(Integer(), nullable=False, autoincrement=True, primary_key=True)
        polling_unit_id = Column(Integer(), nullable=False)
        ward_id = Column(Integer(), nullable=False)
        lga_id = Column(Integer(), nullable=False)
        uniquewardid = Column(Integer(), nullable=True)
        polling_unit_number = Column(String(50), nullable=True)
        polling_unit_name = Column(String(50), nullable=True)
        polling_unit_description = Column(String,nullable=False)
        lat = Column(String(255), nullable=True)
        Long = Column(String(255), nullable=True)
        entered_by_user = Column(String(50), nullable=True)
        date_entered = (DateTime)
        user_ip_address = Column(String(50), nullable=True)

    else:
        uniqueid = 0
        polling_unit_id = 0
        ward_id = 0
        lga_id = 0
        polling_unit_number = ""
        polling_unit_name = ""
        polling_unit_description = ""
        lat = ""
        Long = ""
        entered_by_user = ""
        date_entered = ""
        user_ip_address = ""
        uniquewardid = 0

    def __init__(self, *args, **kwargs):
        """initializes farm user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
