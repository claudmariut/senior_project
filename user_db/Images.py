from tinydb import TinyDB
import cv2
import face_recognition
from PIL import Image, ImageDraw


image_path=["/Users/nathaliebirang/Documents/GitHub/tinydb/Project/main/PoPo.jpeg",]
labels=[1,2]

db = TinyDB('facial recognition_db.json')

def extract_facial_features(path):
    #img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
    # Load the jpg file into a numpy array
   image_path = path
   image = face_recognition.load_image_file(image_path)

    # Find face locations and landmarks (facial features)
   face_locations = face_recognition.face_locations(image)
   face_landmarks_list = face_recognition.face_landmarks(image)

    # Load the image into a PIL (Python Imaging Library) object so we can draw on it
   pil_image = Image.fromarray(image)

    # Create a PIL drawing object to draw on the image
   draw = ImageDraw.Draw(pil_image)

   facailList=[]

    # Loop through each face found in the image
   for (top, right, bottom, left), face_landmarks in zip(face_locations, face_landmarks_list):
        # Draw a rectangle around the face
        draw.rectangle(((left, top), (right, bottom)), outline="red", width=2)

         # Print the location of each facial feature in this image
        for facial_feature in face_landmarks.keys():
            #create a dictionary of key type facial feature name and value to be data points of te facial feature.

            # facialDict={
            #     facial_feature:face_landmarks[facial_feature]
            # }
            facialDic={}

            facialDic=facialDic.update({facial_feature: face_landmarks[facial_feature]})

                
            print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Save or display the modified image
   
   pil_image.show()
    #return the points for all facial features.
   return facialDic

data=[]

for image_path,labels in zip(image_path,labels):

    facial_features=extract_facial_features(image_path)

    print("The {} in this face has the following points:".format(facial_features))

    entry= {
         "label":labels,
         "image_path":image_path,
         "facial_feature":facial_features
    }
    data.append(entry)

db.insert_multiple(data)