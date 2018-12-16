from main import Customer, Company, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///CustomerDatabase.db')

Base.metadata.bind = engine
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()

session.query(Customer).all()
customer = session.query(Customer).first()
print(customer.name)
