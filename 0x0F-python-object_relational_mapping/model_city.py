#!/usr/bin/python3
"""
model_city
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class City(Base):
    """state

    Args:
        Base (class): class
    """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(118), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
