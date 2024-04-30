import cv2
import numpy as np
from tinydb import TinyDB, Query

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
reverse_label_mapping = {next(gen):entry['label'] for entry in db.all()}
print(reverse_label_mapping)

# Initialize Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    # Capture frame from webcam
    ret, frame = cap.read()


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
        #predicted_label, confidence = recognizer.predict(face_roi)

        # Map the recognized label back to the folder name
        recognized_person = reverse_label_mapping.get(predicted_label, "Unknown")

        # Draw rectangle around the face and display the recognized person
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, f"Person: {recognized_person}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Webcam Face Recognition', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()