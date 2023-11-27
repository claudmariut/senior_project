import cv2
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from tinydb import TinyDB, Query

# Path to load the TinyDB database file
from lbphTrainer import label_mapping

database_path = "test_faces_database.json"

# Initialize TinyDB
db = TinyDB(database_path)

# Load the trained recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("lbph_recognizer.yml")

# Lists to store true and predicted labels
true_labels = []
predicted_labels = []

# Query object to check if 'image_paths' key exists
image_paths_key_exists = Query().image_paths.exists()

# Reverse the label mapping to map integer labels back to string identifiers
reverse_label_mapping = {v: k for k, v in label_mapping.items()}
reverse_label_mapping[-1] = '-1'

# Iterate through the database and test the recognizer
for entry in db.all():
    label = entry['label']

    # Check if 'image_paths' key exists in the entry
    if image_paths_key_exists(entry):
        image_paths = entry['image_paths']

        for img_path in image_paths:
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

            # Recognize the face using the trained recognizer
            label, confidence = recognizer.predict(img)

            # Check if the recognizer is confident (confidence >= threshold)
            confidence_threshold = 90  # Adjust this threshold based on your requirements
            if confidence > confidence_threshold:
                label = -1  # Set label to -1 for uncertain predictions

            # Map integer label back to string identifier
            predicted_label_str = reverse_label_mapping[label]

            # Append true and predicted labels to the lists
            true_labels.append(entry['label'])
            predicted_labels.append(predicted_label_str)

# Convert lists to NumPy arrays
true_labels = np.asarray(true_labels)
predicted_labels = np.asarray(predicted_labels)

# Calculate accuracy
accuracy = accuracy_score(true_labels, predicted_labels)
print(f"Accuracy: {accuracy:.2%}")

# Generate and print classification report
print("Classification Report:")
print(classification_report(true_labels, predicted_labels))

# Generate and print confusion matrix
conf_matrix = confusion_matrix(true_labels, predicted_labels)
print("Confusion Matrix:")
print(conf_matrix)

# Release resources
cv2.destroyAllWindows()

# Close the database
db.close()