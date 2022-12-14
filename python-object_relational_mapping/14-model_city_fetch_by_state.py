#!/usr/bin/python3
"Changes the name of a State object from the database"

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # states_with_cities = session.query(
    #     State, City).filter(State.id == City.state_id)

    states_with_cities = session.query(
        State, City).filter(State.id == City.state_id).order_by(City.id)

    for state, city in states_with_cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.commit()
