#!/usr/bin/python3
"""
Prints the State object with the name passed as argument from the database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    search = argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == search)
    if states is not None and states.count() > 0:
        for state in states:
            print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
