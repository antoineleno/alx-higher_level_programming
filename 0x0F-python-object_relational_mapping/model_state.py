#!/usr/bin/python3
"""
model_state
"""
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class State(Base):
        """state

        Args:
            Base (class): class
        """
        __tablename__ = "state"
        id = Column(Integer, autoincrement=True, unique=True, nullable=False, primary_key=True)
        name = Column(String(118), nullable=False)
        
DATABASE_URL = "mysql+mysqlconnector://username:password@localhost:3306/database_name"
engine = create_engine(DATABASE_URL, echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()