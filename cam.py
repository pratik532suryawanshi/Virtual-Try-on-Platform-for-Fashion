import cv2
import pyttsx3
import pyautogui


# Initialize text-to-speech engine
engine = pyttsx3.init()

# Define the desired window width and height (smaller dimensions)
window_width = 640
window_height = 480

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 represents the default camera (you can change this if needed)

# Set the window size
cv2.namedWindow('User Scanner', cv2.WINDOW_NORMAL)
cv2.resizeWindow('User Scanner', window_width, window_height)

# Load a pre-trained face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Define the region of interest (ROI) for scanning
roi_x = 200
roi_y = 150
roi_width = 240  # Reduce the width to make it smaller
roi_height = 180  # Reduce the height to make it smaller

# Ask for camera permission using a dialog box
permission = pyautogui.confirm('Allow access to the camera?', buttons=['Allow', 'Block'])

if permission != 'Allow':
    exit()  # Exit the program if permission is denied

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the ROI
    roi = gray[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]
    faces = face_cascade.detectMultiScale(roi, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw a rectangle to highlight the scanning area
    cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

    if len(faces) > 0:
        # If a user is detected, announce a voice message
        message = "User detected!"
        engine.say(message)
        engine.runAndWait()

    # Add a decorative message to the frame
    message = "Align your face within the rectangle"
    cv2.putText(frame, message, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display the frame with the scanning area and face detection
    cv2.imshow('User Scanner', frame)

    # Exit the loop if the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera, close all OpenCV windows, and stop the text-to-speech engine
cap.release()
cv2.destroyAllWindows()
engine.stop()
