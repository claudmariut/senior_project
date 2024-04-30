import cv2

def set_resolution(cap, width, height):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

def capture_images(num_images=10, save_path="captured_images", width=640, height=480):
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (your webcam)

    # Set the desired resolution
    set_resolution(cap, width, height)

    # Create the save path if it doesn't exist
    import os
    os.makedirs(save_path, exist_ok=True)

    # Capture and save images
    for i in range(num_images):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow("Press any key to capture", frame)

        # Wait for a key press
        cv2.waitKey(0)

        # Save the image in JPG format
        image_filename = f"{save_path}/image_{i+1}.jpg"
        cv2.imwrite(image_filename, frame)

    # Release the capture object and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_images(11, width=1280, height=720)  # Set your desired resolution here