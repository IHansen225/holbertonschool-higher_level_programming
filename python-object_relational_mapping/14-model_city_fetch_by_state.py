#!/usr/bin/python3
"""
    Approach to SQLAlchemy ORM
    First query exercise
"""
from sys import argv
from model_city import City, Base
from model_state import Base, State
from sqlalchemy import create_engine as eng
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update

if __name__ == "__main__":
    engine = eng(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")

    Session = sessionmaker(engine)
    session = Session()

    states_query = session.query(City, State).filter(State.id == City.state_id).all()
    for city, state in states_query:
        print(f"{state.name}: ({city.id}) {state.name}")
