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
    query = session.query(State.name, State.id).order_by(State.id)
    for name, id in query:
        print("{:d}: {:s}".format(id, name))
