from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import Base, Customer, Company

engine = create_engine('sqlite:///CustomerDatabase.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

customerData = Customer(name='Aditya Chaturvedi')
session.add(customerData)
session.commit()

companyData = Company(name='Watermark Insights')
session.add(companyData)
session.commit()
