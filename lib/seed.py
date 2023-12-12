# seeds/seeds.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import Restaurant, Customer, Review

# Replace 'sqlite:///database.sqlite' with the actual database URL
DATABASE_URL = 'sqlite:///database.sqlite'
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Seed data for restaurants
restaurant1 = Restaurant(name='Restaurant1', price=2)
restaurant2 = Restaurant(name='Restaurant2', price=3)

# Seed data for customers
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Doe')

# Seed data for reviews
review1 = Review(star_rating=4, comment='Great experience')
review2 = Review(star_rating=5, comment='Excellent service')

# Establish relationships
review1.restaurant = restaurant1
review1.customer = customer1

review2.restaurant = restaurant2
review2.customer = customer2

# Add seed data to the session
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

# Commit the changes
session.commit()

# Close the session
session.close()
