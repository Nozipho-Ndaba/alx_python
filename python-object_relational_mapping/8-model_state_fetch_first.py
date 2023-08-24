#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)

    Base.metadata.create_all(engine)
    s_tate = session.query(State).order_by(State.id).first()

    if s_tate:
        print("{}: {}".format(s_tate.id, s_tate.name))
    else:
        print("Nothing")
    session.close()
