#!/usr/bin/python3
"""
Lists all State objects that contain the letter a from the database
"""

from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a'))\
                    .order_by(State.id)
    if states is not None:
        for state in states:
            print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
    session.close()
