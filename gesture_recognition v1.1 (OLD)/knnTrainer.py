import cv2
import numpy as np
from tinydb import TinyDB, Query
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib

# Load the TinyDB database
db = TinyDB("gestures_database.json")

# Query object for TinyDB
db_query = Query()

# Lists to store features and corresponding labels
features_list = []
labels_list = []

# Iterate through entries in the database
for entry in db.all():
    # Get gesture name and features from the entry
    gesture_name = entry['gesture_name']
    features = entry['features']

    # Append features and corresponding label to the lists
    features_list.extend(features)
    labels_list.extend([gesture_name] * len(features))

# Convert lists to NumPy arrays
X = np.asarray(features_list)
y = np.asarray(labels_list)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=3)

# Train the classifier
knn_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn_classifier.predict(X_test)

# Evaluate the classifier
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

# Display the results
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)

# Save the trained classifier to a file using joblib
joblib.dump(knn_classifier, "knn_gesture_classifier.joblib")

# Close the TinyDB database
db.close()