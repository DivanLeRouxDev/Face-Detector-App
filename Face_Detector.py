import cv2

#Pre Trained data being used.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#import image
#img = cv2.imread('Robert-Downey.jpg')
#capture video.
webcam = cv2.VideoCapture(0)

while True:
    successful_frame_read, frame = webcam.read()


    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


    for(x, y, w, h ) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3) 


    cv2.imshow('Face Detector App', frame)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break


webcam.release()
print('Code Completed')


"""
grayscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Detect Faces
face_coordinates = trained_face_data.detectMultiScale(grayscale_img)

#Rectangle Over Color Image
for(x, y, w, h ) in face_coordinates:
   cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, randrange(255)), 3) 

#print(face_coordinates)

# Shows app and waits to keep open.
cv2.imshow('Face Detector App', img)
cv2.waitKey()


"""

