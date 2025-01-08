from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create base class for your classes to inherit from
Base = declarative_base()

# Define the Finance model (this class represents the 'users' table in the database)
class Finance(Base):
    __tablename__ = 'users'

    # Columns for the table
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)

    # Define string representation method for easy printing
    def __str__(self):
        return f"User's ID: {self.user_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}"

# Database URL for SQLite database (can be changed to connect to other databases)
DATABASE_URL = 'sqlite:///students.db'

# Create an SQLite database engine (or connect to one)
engine = create_engine(DATABASE_URL)

# Create a session factory that will be used to create session objects
Session = sessionmaker(bind=engine)

# Code to create all tables in the database
if __name__ == '__main__':
    try:
        # Create all tables in the database (this will create the 'users' table for the Finance model)
        Base.metadata.create_all(engine)
        print('Tables created successfully.')
        
        # Create a session object to interact with the database
        session = Session()

        # Example: Adding a new user to the 'users' table
        new_user = Finance(first_name='John', last_name='Doe', email='john.doe@example.com')
        session.add(new_user)
        session.commit()  # Commit the transaction
        
        print(f'New user added: {new_user}')

    except Exception as e:
        print(f'An error occurred: {e}')
    
    finally:
        # Close the session to free resources
        session.close()
        print('Session closed.')
