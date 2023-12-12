Generic single-database configuration.

# Restaurant Review System
  ## Overview

This Python application is a restaurant review system designed for managing restaurant data, customer reviews, and relationships between them. The system uses SQLAlchemy for database interactions, Alembic for database migrations, and Faker for generating seed data. It includes models for Restaurant, Customer, and Review with relationships and methods for efficient querying and manipulation of data.
  ## Table of Contents

    Installation
    Usage
    Migrations
    Models
    Seeding
    Object Relationship Methods
    Aggregate and Relationship Methods
    Developer
    Contributing
    License

## Installation

   ## 1.Clone the repository:

    bash

git clone https://github.com/Muthomi254/Restaurants-code-challange-with-sqlalchemy
cd restaurant-review-system

 ## 2. Install dependencies:

bash

pip install -r requirements.txt

## 3. Configure the database URL in main.py:

python

    # main.py
    DATABASE_URL = 'sqlite:///database.sqlite'

## Usage

## 1. Run the application:

bash

python main.py

## 2. Migrations

Apply migrations using Alembic:

bash

alembic upgrade head

## Models

    Restaurant: Represents a restaurant with attributes name and price.
    Customer: Represents a customer with attributes first_name and last_name.
    Review: Represents a review with attributes star_rating, comment, and relationships with Restaurant and Customer.

## Seeding

Seed the database with sample data:

bash

python lib/seed.py

## Object Relationship Methods

    Review.customer(): Returns the Customer instance for this review.
    Review.restaurant(): Returns the Restaurant instance for this review.
    Restaurant.reviews(): Returns a collection of all the reviews for the restaurant.
    Restaurant.customers(): Returns a collection of all the customers who reviewed the restaurant.
    Customer.reviews(): Returns a collection of all the reviews that the customer has left.
    Customer.restaurants(): Returns a collection of all the restaurants that the customer has reviewed.

## Aggregate and Relationship Methods

    Customer.full_name(): Returns the full name of the customer, with the first name and the last name concatenated.
    Customer.favorite_restaurant(): Returns the restaurant instance that has the highest star rating from this customer.
    Customer.add_review(restaurant, rating): Adds a new review for the restaurant with the given rating.
    Customer.delete_reviews(restaurant): Removes all reviews for the specified restaurant.
    Review.full_review(): Returns a string formatted as a review for a specific restaurant by a specific customer.
    Restaurant.fanciest(): Returns the restaurant instance with the highest price.
    Restaurant.all_reviews(): Returns a list of strings with all the reviews for the restaurant.

## Developer

    Developer: Dan Munene
    Contact: dmunene202020@gmail.com
    GitHub: https://github.com/Muthomi254/Restaurants-code-challange-with-sqlalchemy

## Contributing

    Fork the repository.
    Create a new branch: git checkout -b feature/new-feature.
    Commit your changes: git commit -m 'Add new feature'.
    Push to the branch: git push origin feature/new-feature.
    Submit a pull request.

## License

This project is licensed under the MIT License.