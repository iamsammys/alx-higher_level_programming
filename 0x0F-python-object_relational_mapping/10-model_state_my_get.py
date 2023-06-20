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
    name_match = sys.argv[4]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:\
                           3306/{}".format(user, passwd, db_name))

    Session = sessionmaker(bind=engine)
    session = Session()
    id = session.query(State.id).filter(State.name == name_match).first()
    if id is not None:
        print(id[0])
    else:
        print("Not found")
    session.close()
