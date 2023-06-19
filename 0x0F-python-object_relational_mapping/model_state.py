#!/usr/bin/python3
"""
A python file that contains the class definition of a State
"""
import sqlalchemy
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    A class representing states table
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
