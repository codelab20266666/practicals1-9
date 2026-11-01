"""Practical No. 1 - OpenCV installation and working with Python.

Draws shapes on a blank canvas, runs Canny edge detection, and finds
contours of a white circle.

Originally written for Google Colab; this version runs locally using
normal OpenCV windows. Install the library first with:
    pip install opencv-python
"""
import cv2
import numpy as np

# 1. Create a blank black canvas (Height, Width, Channels)
canvas = np.zeros((400, 600, 3), dtype=np.uint8)

# 2. Draw various shapes using OpenCV
# Draw a Blue Line
cv2.line(canvas, (50, 50), (550, 50), (255, 0, 0), 3)

# Draw a Green Rectangle
cv2.rectangle(canvas, (50, 100), (200, 250), (0, 255, 0), -1)  # -1 fills the shape

# Draw a Red Circle
cv2.circle(canvas, (400, 175), 60, (0, 0, 255), 4)

# Put text on the canvas
cv2.putText(
    canvas,
    "OpenCV in Colab!",
    (150, 350),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.9,
    (255, 255, 255),
    2,
    cv2.LINE_AA,
)

print("--- 1. Generated Shape Canvas ---")
cv2.imshow("1. Generated Shape Canvas", canvas)

# 3. Perform Edge Detection (Canny Edge Detection)
# First, convert the canvas to grayscale
gray_canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detector
edges = cv2.Canny(gray_canvas, threshold1=100, threshold2=200)

print("--- 2. Canny Edge Detection Result ---")
cv2.imshow("2. Canny Edge Detection Result", edges)

# 4. Simple Thresholding & Contour Detection
# Create a binary image with a white circle
circle_img = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(circle_img, (150, 150), 80, 255, -1)

# Find contours of the white circle
contours, hierarchy = cv2.findContours(
    circle_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

print(f"Number of contours found: {len(contours)}")

# Draw the contours back onto a colour image to visualise them
contour_display = cv2.cvtColor(circle_img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(contour_display, contours, -1, (0, 255, 0), 3)

print("--- 3. Contour Detection Result ---")
cv2.imshow("3. Contour Detection Result", contour_display)

print("Press any key on an image window to close all windows.")
cv2.waitKey(0)
cv2.destroyAllWindows()
