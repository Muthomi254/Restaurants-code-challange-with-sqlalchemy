from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review

# Replace 'sqlite:///database.sqlite' with the actual database URL
DATABASE_URL = 'sqlite:///database.sqlite'
engine = create_engine(DATABASE_URL)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()

# Generate a random number of customers, restaurants, and reviews
num_customers = fake.random_int(min=5, max=15)
num_restaurants = fake.random_int(min=5, max=15)
num_reviews = fake.random_int(min=20, max=50)

# Seed data for restaurants
restaurants = [Restaurant(name=fake.company(), price=fake.random_int(min=1, max=5)) for _ in range(num_restaurants)]

# Seed data for customers
customers = [Customer(first_name=fake.first_name(), last_name=fake.last_name()) for _ in range(num_customers)]

# Seed data for reviews
reviews = [
    Review(
        star_rating=fake.random_int(min=1, max=5),
        comment=fake.text(),
        restaurant=fake.random_element(elements=restaurants),
        customer=fake.random_element(elements=customers)
    ) for _ in range(num_reviews)
]

# Add seed data to the session
session.add_all(restaurants + customers + reviews)

# Commit the changes
session.commit()

# Close the session
session.close()
