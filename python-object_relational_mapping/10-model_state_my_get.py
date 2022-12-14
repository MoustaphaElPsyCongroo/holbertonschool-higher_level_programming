#!/usr/bin/python3
"Prints the State object with the name passed as argument"

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).order_by(State.id)
    state = query.filter(State.name.like(argv[4]))

    if state.first() is not None:
        print(state[0].id)
    else:
        print("Not found")
