import cv2
import os

# Create a directory to store captured images
gesture_folder = "gesture_images"
if not os.path.exists(gesture_folder):
    os.makedirs(gesture_folder)

# Open a connection to the webcam (0 is usually the default camera)
cap = cv2.VideoCapture(0)

# Set the width and height of the video capture
cap.set(3, 640)
cap.set(4, 480)

# Define the coordinates for the region of interest (ROI)
roi_x, roi_y, roi_width, roi_height = 200, 100, 200, 200

# Initialize a counter for captured images
image_counter = 0

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Create a copy of the frame to draw the ROI
    frame_with_roi = frame.copy()

    # Draw the ROI rectangle on the frame
    cv2.rectangle(frame_with_roi, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

    # Display the frame with ROI
    cv2.imshow("Hand Gesture Capture", frame_with_roi)

    # Extract the region of interest (hand gesture) from the frame
    roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    # Wait for the user to press 'c' to capture an image
    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        # Save the captured image to the gesture folder
        image_path = os.path.join(gesture_folder, f"gesture_{image_counter}.png")
        cv2.imwrite(image_path, roi)
        print(f"Captured image: {image_path}")
        image_counter += 1

    # Break the loop if the user presses 'q'
    elif key == ord('q'):
        break

# Release the webcam and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()