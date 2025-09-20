#!/usr/bin/python3
"""
This module defines a State class and a Base instance for SQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the Base class
Base = declarative_base()


class State(Base):
    """
    State class mapped to the 'states' table in MySQL.
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
