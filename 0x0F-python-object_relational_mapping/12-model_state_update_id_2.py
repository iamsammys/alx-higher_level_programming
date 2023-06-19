#!/usr/bin/python3
"""
Changes the name of a State objects from the database
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
    try:
        new_state = session.query(State).filter(State.id == 2).one()
        new_state.name = "New Mexico"
    except exception as e:
        print("Not found")
    session.commit()
    session.close()
