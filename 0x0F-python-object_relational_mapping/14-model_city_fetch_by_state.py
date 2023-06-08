#!/usr/bin/python3
"""
Prints all City objects from the database
"""

from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(State.name, City.id, City.name)\
                    .join(State, City.state_id == State.id)\
                    .order_by(City.id)
    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
    session.close
