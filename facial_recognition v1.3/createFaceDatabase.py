import os
from tinydb import TinyDB, Query

# Path to the directory containing subject folders (e.g., s1, s2, ...)
dataset_path = "att_dataset"

# Path to save the TinyDB database file
database_path = "test_faces_database.json"

# Initialize TinyDB
db = TinyDB(database_path)

# Iterate through subject folders
for subject_folder in os.listdir(dataset_path):
    subject_path = os.path.join(dataset_path, subject_folder)

    if os.path.isdir(subject_path):
        # Use folder name as the person's identifier
        identifier = subject_folder

        # Get a list of image paths in the subject folder
        image_paths = [os.path.join(subject_path, filename) for filename in os.listdir(subject_path) if filename.endswith(".pgm")]

        # Insert an entry into the database with label, subject_name, and image_paths
        db.insert({'label': identifier, 'subject_name': subject_folder, 'image_paths': image_paths})

# Close the database
db.close()