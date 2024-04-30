
from tinydb import TinyDB, Query

db = TinyDB('face_gesture_db.json')

# Define a query object for later use
User = Query()

# Function to add a user to the database
def add_user(user_id, facial_features, gesture_label):
    db.insert({'user_id': user_id, 'facial_features': facial_features, 'gesture_label': gesture_label})

# Function to retrieve user information from the database
def get_user(user_id):
    user = db.get(User.user_id == user_id)
    return user

# Example usage
if __name__ == "__main__":
    # Add a user to the database
    add_user(1, {'feature1': 0.8, 'feature2': 0.6}, 'wave')

    # Retrieve user information
    user_info = get_user(1)
    print("User ID:", user_info['user_id'])
    print("Facial Features:", user_info['facial_features'])
    print("Gesture Label:", user_info['gesture_label'])