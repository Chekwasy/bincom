#!/usr/bin/python3
""" holds class announced_state_results"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from hashlib import md5


class announced_state_results(BaseModel, Base):
    """Representation for announced_state_results"""
    if models.storage_t == 'db':
        __tablename__ = 'announced_state_results'
        result_id = Column(Integer(11), nullable=False, autoincrement=True, primary_key=True)
        state_name = Column(String(50), nullable=False)
        party_abbreviation = Column(String(4), nullable=False)
        party_score = Column(Integer(11), nullable=False)
        entered_by_user = Column(String(50), nullable=False)
        date_entered = Column(DateTime, nullable=False)
        user_ip_address = Column(String(50), nullable=False)

    else:
        result_id = ""
        state_name = ""
        party_abbreviation = ""
        party_score = ""
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
