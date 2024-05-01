# **SOURCE CODE FOR INTEGRATION OF MACHINE LEARNING (AI/ML) AND IoT FOR HOME AUTOMATION**
## Project Summary
This project innovatively combines facial and gesture recognition in doorbell cameras, redefining home security. Leveraging LBPH(Local Binary Pattern Histogram) and CNN, the system identifies visitors through facial features and interprets user gestures for intuitive control. The process involves database creation, mobile app development, machine learning model training, and real-time implementation. All integrated  in a Raspberry Pi microcontroller.

## Folder Structure
### Facial Recognition v1.3 (Individual Files used by Backend Server)
__1. captureImages.py__

  - Captures images using your webcam to create a dataset for facial recognition.

__2. createFaceDatabase.py__

  - Creates a TinyDB database from the ATT faces dataset for training facial recognition.

__3. facialDetectionTestPI.py__

  - Uses a Raspberry Pi camera for real-time face detection.

__4. jpgTopgm.py__

  - Converts JPG images to PGM format for compatibility with the ATT faces dataset.

__5. lbphTrainer.py__

  - Trains an LBPH facial recognition model and saves it as a YAML file.

__6. randomPeople.py__

  - Processes images of random people for testing facial recognition.

__7. scanFace.py__
   
 - Uses Haar cascades for face detection from the webcam feed.
    - Usage:
        - Run scanFace.py to access the webcam and detect faces.
        - Adjust the script for specific resolutions or camera settings as needed.
        - Press 'q' to exit the loop.
        - 
__8. verifyFace.py__

  - Verifies faces in real-time using the trained LBPH recognizer.
    - Usage:
        - Ensure the LBPH recognizer is trained using lbphTrainer.py before running.
        - Run verifyFace.py to access the webcam and verify faces.
        - Recognized faces are displayed with a rectangle and person's name.
        - Press 'q' to exit the loop.

__9, verifyFaceStats.py__

  - Evaluates the accuracy and performance of the facial recognition model.
    - Usage:
      - Run verifyFaceStats.py to assess the accuracy, classification report, and confusion matrix.
      - Adjust the confidence threshold in the script based on your requirements.

### Gesture Recognition v1.1 (OLD Version when using KNN instead of CNN) - No required
__1. createGestureDatabase.py__

  - Creates a TinyDB database from a dataset of hand gesture images.

__2. knnTrainer.py__

  - Trains a K-Nearest Neighbors (KNN) classifier for gesture recognition.

__3. newGesture.py__

  - Captures images of hand gestures to add to the gesture dataset.

__4. verifyGesture.py__

  - Verifies hand gestures in real-time using the trained KNN classifier.
    - Usage:
        - Ensure the KNN classifier is trained using knnTrainer.py before running.
        - Run verifyGesture.py to access the webcam and verify hand gestures.
        - Recognized gestures are displayed on the frame.
        - Press 'q' to exit the loop.
          
### Home Assistant and Project Demo
__1. switchLight.py__

  - Controls a smart switch/light using MQTT for Home Assistant Integration.

__2. projectDemo.py__

  - Combines all the Machine Learning Models establishing communication with Home Assistant. (Implement a new Gesture Recognition Model)

__3. restfulAPI.py__

  - (In progress) New alternative to establish a better integration between the AI Module and Home Assistant.

## Dependencies
  - OpenCV
    -     pip install opencv-python
  - scikit-image
    -     pip install scikit-image
  - TinyDB
    -     pip install tinydb
  - scikit-learn
    -     pip install scikit-learn
  - Paho MQTT
    -     pip install paho-mqtt

## Usage
__1. Facial Recognition__

  - Follow the sequence of scripts: __createFaceDatabase.py__ -> __lbphTrainer.py__ -> __verifyFace.py__ -> __verifyFaceStats.py__.
  - Adjust parameters in scanFace.py for specific camera settings.

__2. Gesture Recognition__

  - Follow the sequence of scripts: __createGestureDatabase.py__ -> __knnTrainer.py__ -> __verifyGesture.py__.

__3. Project Demo__

  - Run projectDemo.py, ensure faces database, face recognizer and haar cascade classifier are in the same directory.
  
## Notes
Ensure the dataset directories (__att_dataset__ and __gesture_dataset__) are correctly structured.
Adjust parameters such as image resolution and model settings based on specific requirements.

## Aknowledgments
  - [ATT Faces Database](https://www.kasrl.org/jplab/)
  - [OpenCV](https://opencv.org/)
  - [scikit-image](https://scikit-image.org/)
  - [TinyDB](https://tinydb.readthedocs.io/en/latest/)
  - [scikit-learn](https://scikit-learn.org/stable/)
  - [Paho MQTT](https://pypi.org/project/paho-mqtt/)
