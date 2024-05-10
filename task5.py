import cv2
import face_recognition

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained face recognition model
known_face_encodings = []
known_face_names = []

# Add your known faces and their names
# For example:
# known_face_encodings.append(face_encoding)
# known_face_names.append("John Doe")

# Load the input image or video
input_image = cv2.imread('input_image.jpg')

# Convert the image to grayscale for face detection
gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)

# Perform face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Iterate over detected faces
for (x, y, w, h) in faces:
    # Extract the face region
    face_image = input_image[y:y+h, x:x+w]

    # Encode the face image for recognition
    face_encoding = face_recognition.face_encodings(face_image)[0]

    # Compare the face encoding with known faces
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

    # Find the best match
    name = "Unknown"
    if True in matches:
        match_index = matches.index(True)
        name = known_face_names[match_index]

    # Draw a rectangle around the face and display the name
    cv2.rectangle(input_image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(input_image, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Display the output image
cv2.imshow('Face Detection and Recognition', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()