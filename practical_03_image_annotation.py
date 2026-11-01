"""Practical No. 3 - Image annotation with OpenCV.

Draws a line, rectangle, circle, ellipse and text on a blank white image.
"""
import os

import cv2
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_DIR, "Prac3_output.jpg")

# Create a white image
image = 255 * np.ones((500, 700, 3), dtype="uint8")

# 1. Draw a line
cv2.line(image, (50, 50), (300, 50), (255, 0, 0), 3)

# 2. Draw a rectangle
cv2.rectangle(image, (50, 100), (250, 220), (0, 255, 0), 3)

# 3. Draw a circle
cv2.circle(image, (400, 160), 60, (0, 0, 255), 3)

# 4. Draw an ellipse
cv2.ellipse(image, (550, 160), (70, 40), 0, 0, 360, (255, 0, 255), 3)

# 5. Add text
cv2.putText(
    image,
    "OpenCV Image Annotation",
    (50, 300),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 0),
    2,
)

# Add labels
cv2.putText(image, "Line", (50, 35),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
cv2.putText(image, "Rectangle", (50, 245),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
cv2.putText(image, "Circle", (360, 245),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
cv2.putText(image, "Ellipse", (515, 245),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# Display and save the image
cv2.imshow("Practical 3 - Image Annotation", image)
cv2.imwrite(OUTPUT_PATH, image)

print("Image annotation completed successfully!")
print("Output saved as Prac3_output.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
