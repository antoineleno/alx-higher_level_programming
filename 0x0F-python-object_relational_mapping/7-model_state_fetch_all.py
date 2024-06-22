#!/usr/bin/python3
"""
model_state module
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
import sys

def list_all_states(username, db_password, db_name):
    """list_all_states 

    Args:
        username (string): _description_
        db_password (string): db password
        db_name (string): db name
    """
    
    db_url = f"mysql+mysqlconnector://{username}:{db_password}@localhost:3306/{db_name}"
    engine = create_engine(db_url,echo=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(state)

    

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    else:
        list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
