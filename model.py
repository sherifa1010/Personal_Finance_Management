from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#create base class for your classes to inherit from
Base = declarative_base()

class Finance(Base):
  __tablename__ = 'users'

  #columns for the table
  user_id = Column(Integer, primary_key=True)
  first_name = Column(String(50), nullable=False) 
  last_name = Column(String(50), nullable=False) 
  email = Column(String(50), nullable=False, unique=True)

  #Define string representation method for easyprinting
  def __str__(self):
    return f"User's ID: {self.user_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}."
    
    # Create an SQLite database engine (or connect to one)
    DATABASE_URL = 'sqlite:///students.db'
    engine = create_engine(DATABASE_URL)

    # CREATE A SESSION FACTORY
    session = sessionmaker(bind=engine)
    session = Session()

    # Code to create all tables in the database
    if __name__ == '__main__':
        try:
            #create all tables in the database
            Base.metadata.create_all(engine)
            print('Tables created successfully.')
        except Exception as e:
            print(f'An error occurred: {e}.')