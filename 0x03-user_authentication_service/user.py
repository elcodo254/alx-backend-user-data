#!/usr/bin/env python3
"""
class user for ORM
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    represents user
    attributes: id - integer primary key
                email - non-nullable string
                hashed_paasword - non-nullable string
                session_id - nullable string
                reset_token - nullable string
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))
