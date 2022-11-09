#!/usr/bin/python3
"""
    Approach to SQLAlchemy ORM
    First query exercise
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine as eng
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = eng(f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}")

    Session = sessionmaker(engine)
    session = Session()

    states_query = session.query(City, State).filter(
        City.state_id == State.id
    ).order_by(City.id)
    for state, city in states_query:
        print(f"{city.name}: ({state.id}) {state.name}")
