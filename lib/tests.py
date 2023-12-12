# test.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Replace 'sqlite:///database.sqlite' with the actual database URL
DATABASE_URL = 'sqlite:///database.sqlite'
engine = create_engine(DATABASE_URL, echo=True)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Query and print tables
restaurants = session.query(Restaurant).all()
customers = session.query(Customer).all()
reviews = session.query(Review).all()

print("Restaurants:")
for restaurant in restaurants:
    print(restaurant.id, restaurant.name, restaurant.price)

print("\nCustomers:")
for customer in customers:
    print(customer.id, customer.first_name, customer.last_name)

print("\nReviews:")
for review in reviews:
    print(review.id, review.star_rating, review.comment, review.restaurant.name, review.customer.full_name())
