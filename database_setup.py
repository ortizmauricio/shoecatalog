import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable = False)
    email = Column(String(250), nullable = False)
    picture = Column(String(250))


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable = False)
    user_id =  Column(Integer, ForeignKey('users.id'))
    user =  relationship(Users)

class Model(Base):
    __tablename__ = 'model'

    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
    color = Column(String(15))
    price = Column(String(15))
    condition = Column(String(15))
    resell_price = Column(String(15))
    brand_id = Column(Integer, ForeignKey('brand.id'))
    brand = relationship(Brand)
    user_id =  Column(Integer, ForeignKey('users.id'))
    user =  relationship(Users)

    @property
    def serialize(self):
       return {
           'name': self.name,
           'brand': self.brand.name,
           'id': self.id,
           'color': self.color,
           'condition': self.condition,
           'resell-price': self.resell_price
       }




engine = create_engine('sqlite:///shoecatalogwithusers.db')


Base.metadata.create_all(engine)