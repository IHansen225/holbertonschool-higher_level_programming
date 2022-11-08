#!/usr/bin/python3
"""
    Base model class for ORM
    instance methods
"""
import sys
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        Base constructor for query methods
    """
    __tablename__ = 'states'

    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    name = sa.Column(sa.String(128), nullable=True)


if __name__ == '__main__':
    pass
