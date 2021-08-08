#!/usr/bin/python3
"""Show states content
"""
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format("root", "root", "my_db"),
                       pool_pre_ping=True)

Base.metadata.create_all(engine)

session = sessionmaker(engine)
session = Session()

for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))

session.close()
