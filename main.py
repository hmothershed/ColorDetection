# Multiple Color Detection in Real-Time
import cv2
from color_detection import *
from color_contours import *

# Define colors and corresponding bounding box colors
colors = {
    #               lower value                        upper value                    BGR value
    "red": (np.array([136, 87, 111], np.uint8), np.array([180, 255, 255], np.uint8), (0, 0, 255)),
    "green": (np.array([25, 52, 72], np.uint8), np.array([102, 255, 255], np.uint8), (0, 255, 0)),
    "blue": (np.array([94, 80, 2], np.uint8), np.array([120, 255, 255], np.uint8), (255, 0, 0)),
    "black": (np.array([0, 0, 0], np.uint8), np.array([180, 255, 30], np.uint8), (0, 0, 0)),
    "white": (np.array([0, 0, 231], np.uint8), np.array([180, 30, 255], np.uint8), (255, 255, 255)),
    "brown": (np.array([0, 20, 50], np.uint8), np.array([25, 255, 255], np.uint8), (0, 140, 255)),
    "yellow": (np.array([20, 100, 100], np.uint8), np.array([30, 255, 255], np.uint8), (0, 255, 255)),
    "orange": (np.array([5, 100, 100], np.uint8), np.array([15, 255, 255], np.uint8), (0, 165, 255)),
    "gray": (np.array([0, 0, 50], np.uint8), np.array([180, 20, 150], np.uint8), (128, 128, 128)),
    "purple": (np.array([125, 50, 50], np.uint8), np.array([150, 255, 255], np.uint8), (128, 0, 128))
}

# Initialize webcam
webcam = cv2.VideoCapture(0)

while(1):
    # Read image frame from webcam
    _, imageFrame = webcam.read()

    # Convert image frame to HSV color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Detect colors and get their contours
    color_contours = {}
    for color_name, (lower, upper, bounding_box_color) in colors.items():
        color_mask = detect_color(hsvFrame, lower, upper)
        # apply morphological transform, dialtion for each color and bitwise_and operator
        # between imageFrame to determine mask detected for that particular color.
        kernel = np.ones((5,5), np.uint8)
        color_mask = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, kernel)
        color_mask = cv2.dilate(color_mask, kernel, iterations=1)
        color_frame = cv2.bitwise_and(imageFrame, imageFrame, mask=color_mask)
        contours = get_contours(color_name, color_frame, color_mask)
        color_contours[color_name] = (contours, bounding_box_color)

    # Draw bounding boxes and color names for each detected color
    for color_name, (contours, bounding_box_color) in color_contours.items():
        for contour in contours:
            (x, y, w, h) = cv2.boundingRect(contour)
            cv2.rectangle(imageFrame, (x, y), (x + w, y + h), bounding_box_color, 2)
            cv2.putText(imageFrame, color_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, bounding_box_color, 2)

    # Display the resulting image frame
    cv2.imshow("Color Detection", imageFrame)

    # Check for user input to quit the program
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release the webcam and close all windows
webcam.release()
cv2.destroyAllWindows()
