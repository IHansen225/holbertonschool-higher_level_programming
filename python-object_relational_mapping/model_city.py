#!/usr/bin/python3
"""
    Base model class for ORM
    instance methods
"""
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        Base constructor for query methods
    """
    __tablename__ = 'cities'

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    name = sa.Column(sa.String(128), nullable=True)
    state_id = sa.Column(sa.Integer, ForeignKey("states.id"), nullable=False)
