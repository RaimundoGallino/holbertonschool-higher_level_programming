#!/usr/bin/python3
"""Show states content
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    element = session.query(State).filter(State.id.in_(['1'])).first()
    if element:
        print("{}: {}".format(element.id, element.name))
    else:
        print("Nothing")

    session.close()
