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

    search = argv[4]

    element = session.query(State).filter_by(name=argv[4]).first()
    if element:
        print(element.id)
    else:
        print("Not Found")

    session.close()
