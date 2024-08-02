import cv2
import numpy as np

# Define the lower and upper bounds for the colors (in HSV)
# Adjust these values based on the specific colors of your cubes/squares
color_ranges = {
    'red': ([0, 70, 50], [10, 255, 255]),
    'green': ([35, 100, 50], [85, 255, 255]),
    'blue': ([100, 150, 0], [140, 255, 255]),
    'yellow': ([25, 150, 50], [35, 255, 255])
}

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Iterate over the defined colors
    for color, (lower, upper) in color_ranges.items():
        # Create numpy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")

        # Find the colors within the specified boundaries and apply the mask
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask=mask)

        # Find contours
        contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw rectangles around detected objects
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Filter out small areas
                x, y, w, h = cv2.boundingRect(contour)
                if abs(w - h) < 10:  # Ensure it's a square
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Frame', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
