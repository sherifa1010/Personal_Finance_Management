# Importing session from config and Finance model from model
from configs import session
from model import Finance  # Assuming you have a 'Finance' or 'User' model for storing user data

class SystemCrud:
    def __init__(self):
        """
        Initializes the SystemCrud class and sets up the session for database interaction.
        """
        self.session = session  # Store the session to interact with the database

    def insert_users(self, first_name, last_name, email):
        """
        Insert a new user into the database with the provided details.

        Parameters:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email of the user.

        Returns:
            str: A message indicating the user was added successfully.
        """
        # Creating a new user object from the Finance model
        new_user = Finance(first_name=first_name, last_name=last_name, email=email)

        # Adding the new user to the session and committing to the database
        self.session.add(new_user)  
        self.session.commit()

        # Return a message confirming the user has been added
        return f'New user with these details: {new_user.first_name} {new_user.last_name} was added.'

    def get_all_users(self):
        """
        Fetch all users from the database.

        Returns:
            list: A list of all user objects from the database.
        """
        # Querying all users from the Finance model
        return self.session.query(Finance).all()

    def get_users_by_first(self, first_name):
        """
        Fetch users by their first name.

        Parameters:
            first_name (str): The first name of the user(s) to be retrieved.

        Returns:
            list: A list of user objects that match the first name.
        """
        # Querying users whose first name matches the provided one
        return self.session.query(Finance).filter_by(first_name=first_name).all()  # Use .all() to fetch all matching users

    def get_users_by_id(self, user_id):
        """
        Fetch a user by their unique ID.

        Parameters:
            user_id (int): The ID of the user to be retrieved.

        Returns:
            object: A user object if found, otherwise None.
        """
        # Querying the user by their unique ID
        return self.session.query(Finance).filter_by(user_id=user_id).first()  # Use .first() to fetch only the first result (or None)

    def update_users(self, user_id, first_name=None, last_name=None, email=None):
        """
        Update the details of an existing user by their ID.

        Parameters:
            user_id (int): The ID of the user to be updated.
            first_name (str, optional): The new first name of the user.
            last_name (str, optional): The new last name of the user.
            email (str, optional): The new email of the user.

        Returns:
            str: A message indicating whether the user was updated or not found.
        """
        # Fetch the user by their ID
        selected_user = self.session.query(Finance).filter_by(user_id=user_id).first()

        if selected_user:  # If the user exists, update their details
            # If a new first name is provided, update it
            if first_name:
                selected_user.first_name = first_name
            # If a new last name is provided, update it
            if last_name:
                selected_user.last_name = last_name
            # If a new email is provided, update it
            if email:
                selected_user.email = email

            # Commit the changes to the database
            self.session.commit()

            # Return a success message
            return f'User with ID {user_id} has been updated.'
        
        # If the user is not found, return an error message
        return f'User with ID {user_id} not found.'

# Example usage of the SystemCrud class
if __name__ == "__main__":  # Only run this part if the script is executed directly
    # Initialize the CRUD class
    system_crud = SystemCrud()

    # Insert a new user
    user_1 = system_crud.insert_users('Ama', 'Attu', 'ama@gmail.com')
    print(user_1)  # Print the result of adding a new user

    # Get all users
    all_users = system_crud.get_all_users()
    for user in all_users:  # Loop through each user and print their details
        print(f'User ID: {user.user_id}, Name: {user.first_name} {user.last_name}, Email: {user.email}')

    # Get a user by ID
    user_id = system_crud.get_users_by_id(1)
    if user_id:
        print(f'User with ID 1: {user_id.first_name} {user_id.last_name}')  # Print user details if found
    else:
        print('User not found')  # If no user is found with the given ID

    # Update a user
    updated_user = system_crud.update_users(1, first_name='Ama', last_name='Attu', email='updated_email@gmail.com')
    print(updated_user)  # Print the result of updating the user
