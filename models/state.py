#!/usr/bin/python3
"""State Module for HBNB project"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel


class State(BaseModel, Base):
    """State class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
