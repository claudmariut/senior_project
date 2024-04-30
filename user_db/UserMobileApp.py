from tinydb import TinyDB, Query

# Create or open the database file
db = TinyDB('users.json')

# Define a table for storing user information
users_table = db.table('users')

# Function to register a new user
def register_user(username, password):
    # Check if the username already exists
    if users_table.contains(Query().username == username):
        print("Username already exists. Please choose a different one.")
        return False
    else:
        # Insert new user into the database
        users_table.insert({'username': username, 'password': password})
        print("User registered successfully.")
        return True

# Function to authenticate a user
def authenticate_user(username, password):
    # Check if the username exists in the database
    if users_table.contains(Query().username == username):
        # Get the user's password
        stored_password = users_table.get(Query().username == username)['password']
        # Check if the provided password matches the stored password
        if password == stored_password:
            print("Authentication successful. Welcome, {}!".format(username))
            return True
        else:
            print("Incorrect password.")
            return False
    else:
        print("Username not found.")
        return False

# Example usage
if __name__ == "__main__":
    # Register a new user
    register_user("user1", "password123")

    # Authenticate the user
    authenticate_user("user1", "password123")
