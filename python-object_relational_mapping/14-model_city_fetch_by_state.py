#!/usr/bin/python3
"""Module joining 2 tables: cities and states"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = (
        session.query(City, State)
        .join(State)
        .order_by(City.id.asc())
        .all()
    )

    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
