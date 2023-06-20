#!/usr/bin/python3
"""
script that adds the State object to the database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format
                           (user, passwd, db))
    Session = sessionmaker(bind=engine)
    session = Session()

    new_user = State(name="Louisiana")
    session.add(new_user)
    session.commit()
    print(new_user.id)
    session.close()
