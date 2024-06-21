#!/usr/bin/python3

""" print state object with the name passed as arg from the database """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    stateUpdated = session.query(State).filter(State.id == 2).first()

    if stateUpdated:
        stateUpdated.name = 'New Mexico'
        session.commit()
