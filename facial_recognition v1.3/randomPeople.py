import cv2
import os

# Path to the directory containing JPG images
input_directory = "random_people"

# Path to the directory to save processed images
output_directory = "Unknown"

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Initialize Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iterate through JPG images in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith(".png"):
        # Read the image
        img_path = os.path.join(input_directory, filename)
        img = cv2.imread(img_path)

        # Convert the image to grayscale for face detection
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

        # Process each detected face
        for i, (x, y, w, h) in enumerate(faces):
            # Crop and resize the face region to match the size of pgm files in the ATT dataset
            face_roi = cv2.resize(gray[y:y+h, x:x+w], (92, 112))

            # Save each processed face as a separate PGM image
            output_path = os.path.join(output_directory, f"{filename.split('.')[0]}_face_{i + 1}.pgm")
            cv2.imwrite(output_path, face_roi, [int(cv2.IMWRITE_PXM_BINARY), 1])

# Destroy any OpenCV windows
cv2.destroyAllWindows()