from tinydb import TinyDB, Query

# Create or open the database file
db = TinyDB('user_database.json')

# Define the User table schema
users_table = db.table('nathalie')
User = Query()


def add_user(user_id, name):
    users_table.insert({'id': user_id, 'name': name})

def get_user(user_id):
    user = users_table.get(User.id == user_id)
    return user


def doorbell_user_detected(user_id, user_name):
    add_user(user_id, user_name)
    print(f"User {user_name} with ID {user_id} detected at the door.")


doorbell_user_detected(1, 'Nathalie Birang')



def check_user(user_id):
    user = get_user(user_id)
    if user:
        print(f"Welcome back, {user['name']}!")
        # Trigger automation for a recognized user
    else:
        print("Unknown user. Access denied.")
       
check_user(1)
