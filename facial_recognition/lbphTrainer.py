import cv2
import numpy as np
from tinydb import TinyDB, Query

# Path to load the TinyDB database file
database_path = "att_faces_database.json"

# Initialize TinyDB
db = TinyDB(database_path)

# Create LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Lists to store face samples and corresponding labels
faces = []
labels = []

# Query object to check if 'image_paths' key exists
image_paths_key_exists = Query().image_paths.exists()

# Create a mapping between folder names and unique integer labels
label_mapping = {}

# Function to get or create a unique label for a folder name
def get_label(folder_name):
    if folder_name not in label_mapping:
        label_mapping[folder_name] = len(label_mapping) + 1
    return label_mapping[folder_name]

# Iterate through the database and extract faces, labels, and image paths
for entry in db.all():
    label = entry['label']

    # Check if 'image_paths' key exists in the entry
    if image_paths_key_exists(entry):
        image_paths = entry['image_paths']

        # Convert label to integer using the mapping function
        label = get_label(label)

        for img_path in image_paths:
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            # Append face and label to the lists
            faces.append(img)
            labels.append(label)

# Convert faces and labels lists to NumPy arrays
faces = np.asarray(faces)
labels = np.asarray(labels)

# Train the recognizer
recognizer.train(faces, labels)
print(label_mapping)
# Save the trained recognizer to a file
recognizer.save("lbph_recognizer.yml")

# Release resources
cv2.destroyAllWindows()