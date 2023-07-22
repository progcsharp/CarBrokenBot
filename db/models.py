from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, \
    Integer, String, Boolean, Enum, ForeignKey,\
    MetaData
# Pay attentions if you use another DB like Oracle, MySQL etc.
# This types implement for specific dialect
from sqlalchemy.dialects.postgresql import JSONB, FLOAT

from sqlalchemy.orm import relationship

from .utils import conventions, CategoryEnum


meta = MetaData(naming_convention=conventions)

Base = declarative_base(metadata=meta)


class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    tg_id = Column(Integer)

    def __init__(self, tg_id):
        self.tg_id = tg_id


class Code(Base):
    __tablename__ = 'Code'

    id = Column(Integer, primary_key=True)
    car = Column(Integer)
    code =Column(String)
    description = Column(String)

    def __init__(self, car, code, description):
        self.car = car
        self.code = code
        self.description = description


class Car(Base):
    __tablename__ = 'Car'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name
