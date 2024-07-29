from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Corrected connection string
# SQLALCHEMY_DATABASE_URL = 'postgresql://admin:admin@123@localhost/CollegeData' 
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Admin@localhost/CollegeData'


# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for the declarative base class
Base = declarative_base()

# Dependency to get the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
