import cv2
import picamera
import picamera.array
import numpy as np

# Load the pre-trained cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Initialize the Raspberry Pi camera
with picamera.PiCamera() as camera:
    camera.resolution = (680, 360)

    # Create an array to store the image data
    with picamera.array.PiRGBArray(camera) as output:
        while True:
            # Capture the frame from the camera
            camera.capture(output, format='bgr')
            frame = output.array

            # Convert the frame to grayscale for Haar cascades
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Perform face detection
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

            # Display the frame with detected faces
            cv2.imshow('Detected Faces', frame)

            # Clear the stream in preparation for the next frame
            output.truncate(0)

            # Press 'q' to exit the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# Close all OpenCV windows
cv2.destroyAllWindows()