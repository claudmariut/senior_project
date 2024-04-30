import cv2
import numpy as np
import joblib
from tinydb import TinyDB
from skimage.feature import hog
from skimage import exposure

def extract_features_from_gray_roi(gray_roi):
    # Resize the image to a fixed size (adjust as needed)
    image = cv2.resize(gray_roi, (64, 128))

    # Calculate HOG features
    features = hog(image, orientations=8, pixels_per_cell=(8, 8),
                   cells_per_block=(1, 1), block_norm='L2-Hys', feature_vector=True)

    # Enhance the contrast of the HOG features
    features = exposure.rescale_intensity(features, in_range=(0, 10))

    # Return the HOG features
    return features.tolist()

# Load the trained KNN classifier
knn_classifier = joblib.load("knn_gesture_classifier.joblib")

# Create a list to store the mapping between class labels and gesture names
label_mapping = []

# Load the TinyDB database to get the mapping
db = TinyDB("gestures_database.json")
for entry in db.all():
    label_mapping.append(entry['gesture_name'])
db.close()

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Define the coordinates of the region of interest (ROI)
roi_x, roi_y, roi_width, roi_height = 100, 100, 200, 200

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Extract the region of interest (ROI) from the frame
    roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    # Convert the ROI to grayscale
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Extract features from the ROI using your predefined function
    features = extract_features_from_gray_roi(gray_roi)

    # Reshape the features to match the input shape expected by the classifier
    features = np.reshape(features, (1, -1))

    # Predict the gesture label
    predicted_label_index = knn_classifier.predict(features)[0]

    # Map the predicted label index to the corresponding gesture name
    predicted_gesture = label_mapping[int(predicted_label_index)]

    # Display the predicted gesture on the frame
    cv2.putText(frame, f"Gesture: {predicted_gesture}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Draw a rectangle around the ROI
    cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Gesture Recognition", frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()