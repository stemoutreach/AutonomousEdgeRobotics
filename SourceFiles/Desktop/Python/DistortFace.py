import cv2
import numpy as np

# Load the Haar cascade file for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def distort_face(image, face_coords):
    (x, y, w, h) = face_coords
    face_region = image[y:y+h, x:x+w]
    distorted_face = apply_bulge_effect(face_region)
    image[y:y+h, x:x+w] = distorted_face

def apply_bulge_effect(face_region):
    rows, cols, _ = face_region.shape
    map_x = np.zeros((rows, cols), np.float32)
    map_y = np.zeros((rows, cols), np.float32)

    for i in range(rows):
        for j in range(cols):
            offset_x = j - cols / 2
            offset_y = i - rows / 2
            distance = np.sqrt(offset_x**2 + offset_y**2)
            if distance == 0:
                map_x[i, j] = j
                map_y[i, j] = i
            else:
                r = distance / (cols / 2)
                theta = np.arctan2(offset_y, offset_x)
                r = np.sqrt(r)
                new_x = r * np.cos(theta) * (cols / 2) + (cols / 2)
                new_y = r * np.sin(theta) * (rows / 2) + (rows / 2)
                map_x[i, j] = new_x
                map_y[i, j] = new_y

    distorted_face = cv2.remap(face_region, map_x, map_y, interpolation=cv2.INTER_LINEAR)
    return distorted_face

# Initialize the video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        distort_face(frame, (x, y, w, h))

    cv2.imshow('Distorted Face', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
