import os
from tinydb import TinyDB
import cv2
from skimage.feature import hog
from skimage import exposure
import numpy as np

def extract_features(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image to a fixed size (adjust as needed)
    image = cv2.resize(image, (64, 128))

    # Calculate HOG features
    features = hog(image, orientations=8, pixels_per_cell=(8, 8),
                   cells_per_block=(1, 1), block_norm='L2-Hys', feature_vector=True)

    # Enhance the contrast of the HOG features
    features = exposure.rescale_intensity(features, in_range=(0, 10))

    # Return the HOG features
    return features.tolist()

# Path to the root directory of the gesture dataset
dataset_root = "gesture_dataset"

# Path to save the TinyDB database file
db_path = "gestures_database.json"

# Initialize TinyDB
db = TinyDB(db_path)

# Iterate through subdirectories in the dataset root
for gesture_folder in os.listdir(dataset_root):
    gesture_path = os.path.join(dataset_root, gesture_folder)

    # Check if the item is a directory
    if os.path.isdir(gesture_path):
        # Get a list of image paths in the gesture folder
        image_paths = [os.path.join(gesture_path, filename) for filename in os.listdir(gesture_path) if filename.endswith(('.jpg', '.png'))]

        # Extract features for each image (replace with your own feature extraction logic)
        features = [extract_features(image_path) for image_path in image_paths]

        # Insert an entry into the database with gesture name and extracted features
        db.insert({'gesture_name': gesture_folder, 'features': features})

# Close the database
db.close()

print(f"Gesture dataset information with extracted features has been stored in the TinyDB database: {db_path}")