#!/usr/bin/python3
"""
    Approach to SQLAlchemy ORM
    First query exercise
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(f"\
    mysql+mysqldb://{sys.argv[1]}:\
    {sys.argv[2]}@localhost/{sys.argv[3]}""",
    pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(engine)

