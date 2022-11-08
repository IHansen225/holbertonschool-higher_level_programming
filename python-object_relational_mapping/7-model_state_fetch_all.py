#!/usr/bin/python3
"""
    Approach to SQLAlchemy ORM
    First query exercise
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(f"\
    mysql+mysqldb://{sys.argv[1]}:\
    {sys.argv[2]}@localhost/{sys.argv[3]}""",
    pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    states_query = session.query(State).all()
    for i in states_query:
        print(f"{i.id}: {i.name}")
