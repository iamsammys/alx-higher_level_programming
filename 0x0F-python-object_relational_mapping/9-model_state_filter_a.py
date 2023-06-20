#!/usr/bin/python3
"""
A script that lists all State objects from the database
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    passwd = sys.argv[2]
    user = sys.argv[1]
    db_name = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:\
                           3306/{}".format(user, passwd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)
    for states in state:
        print("{:d}: {:s}".format(states.id, states.name))
    session.close()
