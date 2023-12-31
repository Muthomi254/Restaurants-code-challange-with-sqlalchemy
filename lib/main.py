# main.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Replace 'sqlite:///database.sqlite' with the actual database URL
DATABASE_URL = 'sqlite:///database.sqlite'  # Or use 'sqlite:///database.sqlite' if it's the correct path
engine = create_engine(DATABASE_URL, echo=True)

# Bind the engine to the Base class
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
