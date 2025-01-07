from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Connection string to the MySQL database
connection_str = 'mysql+mysqlconnector://sherry:sherry@localhost/Finance'

# Create the SQLAlchemy engine
engine = create_engine(connection_str)

# Create sessionmaker instance and bind the engine to it
#This session will be used to execute ORM queries and interact with the database
Session = sessionmaker(bind=engine)

# Establish a session
session = Session()

try:
    # Try connecting to the database
    connection = engine.connect()
    print('Located and connected to the database')
    connection.close()  # Close the connection after checking

    # Use the session to interact with the database
    # For example, you could query tables or perform other database operations here
    # session.query(YourModel).all()

except SQLAlchemyError as e:
    print(f'An error occurred: {e}')
finally:
    # Always close the session when done
    session.close()
