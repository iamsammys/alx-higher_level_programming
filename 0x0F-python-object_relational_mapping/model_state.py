#!/usr/bin/python3
"""python script that contains the class definition of
a State and an instance Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column

Base = declarative_base()


class State(Base):
    """representation for states
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
