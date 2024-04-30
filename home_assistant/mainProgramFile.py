import cv2
import mediapipe as mp
import tinydb
from tinydb import TinyDB, Query
from callServices import *
import threading
import time

def call_services_with_delay(delay, entity_id, domain, service_call):
    "To avoid API Blockage"
    while True:
        call_service(entity_id, domain, service_call)
        time.sleep(delay)

thread = threading.Thread(target=call_services_with_delay, args=(5,))
thread.start()

# Initialize MediaPipe Hand module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Gesture mapping
GESTURES = {
    0: "Fist",
    1: "One finger up",
    2: "Two fingers up",
    3: "Three fingers up",
    4: "Four fingers up",
    5: "Five fingers up",
}

gesture_id_global = 0

dbMap = TinyDB("mapping_db.json")

def get_service_parameters(gesture_id):
    # Assuming '_default' is the key for default parameters
    gesture_data = dbMap.get(tinydb.Query()._default[str(gesture_id)])
    if gesture_data:
        return gesture_data['domain'], gesture_data['entity_id'], gesture_data['service']
    else:
        # If gesture_id is not found, return None
        return None, None, None

# Path to load the trained LBPH recognizer file
recognizer_path = "lbph_recognizer.yml"

# Initialize LBPH Face Recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(recognizer_path)

# Load the label mapping from the TinyDB database
database_path = "att_faces_database.json"
db = TinyDB(database_path)

def entries():
    for i in range(1, 100):
        yield i

# Create a reverse mapping from integer labels to folder names
gen = entries()
reverse_label_mapping = {next(gen): entry['label'] for entry in db.all()}
# print(reverse_label_mapping)

# Initialize Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# OpenCV setup for webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # set width
cap.set(4, 480)  # set height

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Hand module
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Extract Y-coordinate of each fingertip
            finger_y = [landmarks.landmark[i].y for i in range(4, 21, 4)]

            # Determine the gesture based on finger positions
            gesture_id = sum(1 for y in finger_y if y < finger_y[0])
            gesture_id_global = gesture_id
            # Display the gesture
            cv2.putText(frame, GESTURES.get(gesture_id, "Unknown"), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Draw hand landmarks on the frame
            for lm in landmarks.landmark:
                h, w, c = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face region
        face_roi = cv2.resize(gray[y:y+h, x:x+w], (92, 112))

        # Save the face region as a PGM file (for debugging or analysis)
        cv2.imwrite("face.pgm", face_roi, [int(cv2.IMWRITE_PXM_BINARY), 1])

        # Recognize the face using the trained LBPH recognizer
        predicted_label, confidence = recognizer.predict(cv2.imread("face.pgm", cv2.IMREAD_GRAYSCALE))
        print(predicted_label)
        confidence_threshold = 90  # Adjust this threshold based on your requirements
        if confidence > confidence_threshold:
            predicted_label = -1  # Set label to -1 for uncertain predictions

        # Map the recognized label back to the folder name
        recognized_person = reverse_label_mapping.get(predicted_label, "Unknown")

        if recognized_person != "Unknown":
            # Call functions based on gestures
            for gesture_id in range(6):  # Assuming there are 6 possible gestures
                if gesture_id == gesture_id_global:
                    domain, entity_id, service_call = get_service_parameters(gesture_id)
                    if domain and entity_id and service_call:
                        call_services_with_delay(delay=5, entity_id=entity_id, domain=domain, service_call=service_call)

        # Draw rectangle around the face and display the recognized person
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, f"Person: {recognized_person}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Combined Recognition', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()