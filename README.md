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
          
### Home Assistant and Project Demo (PC Based)
__1. get_entities.py__

  - Connects to Home Assistant Server and requests all entities information from local network.

__2. get_services.py__

  - Connects to Home Assistant Server and requests all services information.

__3. entitiesDB.py and entities_db.json__ 

  - Uses get_entities.py to create/update a new TinyDB database called entities_db.

__4. servicesDB.py and services_db.json__ 

  - Uses get_entities.py to create/update a new TinyDB database called services_db.

__5. gestureMatching.py__ 

  - Demo that runs on the terminal simulating mobile application gesture mapping with entity/ies and service call selection.

__6. callServices.py__ 

  - Function to execute a service on Home Assistant server. Requires domain, entity id and service call information (Used by Main Program File).

__7. mapping_db.json__ 

  - Mapping database, used by backend server and mobile application to store user configuration about the relation between gestures, entities and services.

__8. mainProgramFile.py__ 

  - Main Program File that runs the AI Module on the backend server. (This version can be run on PC for demo purposes)
  - If used for demo, make sure dependencies are install and you first run the facial recognition files to update the facial recognizer.
  - This file requires the different yml files on the directory as well as json files to work.


### Mobile Application
__Contains a REAMDE file with a link to the source code and mobile application. Another README file can be found on the mobile application folder.__

### Backend Server
__Contains a REAMDE file with a link to the source code and backend server. Another README file can be found on the backend server folder.__

### Live Demo Old (Old PC based demo using KNN - Discontinued)


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
    - 
  
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
