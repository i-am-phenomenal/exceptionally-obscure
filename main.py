import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Customer(Base):
     __tablename__ = 'customer'
     id = Column(Integer, primary_key=True)
     name = Column(String, nullable=False)

class Company(Base):
     __tablename__ = 'company'

     id = Column(Integer, primary_key=True)
     name = Column(String, nullable=False)
     customer_id = Column(Integer, ForeignKey('customer.id'))
     customer = relationship(Customer)

engine = create_engine('sqlite:///CustomerDatabase.db')

Base.metadata.create_all(engine)
