"""Practical No. 2 - Basic image processing with OpenCV.

Steps: load, resize, crop, grayscale, threshold, contours, blob detection.
Place sample.jpg in the same folder as this script.
"""
import os

import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "sample.jpg")


def out(name):
    """Path for an output file, next to this script."""
    return os.path.join(BASE_DIR, name)


# Load the image
image = cv2.imread(IMAGE_PATH)
if image is None:
    print("Error: Image not found!")
    print("Place sample.jpg in the same folder as this script.")
    raise SystemExit(1)

print("Image loaded successfully!")
print("Original image size:", image.shape)

# 1. Display original image
cv2.imshow("Original Image", image)

# 2. Resize image
resized = cv2.resize(image, (400, 300))
cv2.imshow("Resized Image", resized)
cv2.imwrite(out("resized.jpg"), resized)

# 3. Crop image (central region)
height, width = image.shape[:2]
cropped = image[height // 4:3 * height // 4, width // 4:3 * width // 4]
cv2.imshow("Cropped Image", cropped)
cv2.imwrite(out("cropped.jpg"), cropped)

# 4. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", gray)
cv2.imwrite(out("grayscale.jpg"), gray)

# 5. Apply thresholding
_, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("Threshold Image", threshold)
cv2.imwrite(out("threshold.jpg"), threshold)

# 6. Find contours
edges = cv2.Canny(gray, 100, 200)
contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
cv2.imshow("Contours", contour_image)
cv2.imwrite(out("contours.jpg"), contour_image)

# 7. Blob detection
params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 20
params.maxArea = 5000
params.filterByCircularity = False
params.filterByConvexity = False
params.filterByInertia = False

detector = cv2.SimpleBlobDetector_create(params)
keypoints = detector.detect(gray)

blob_image = cv2.drawKeypoints(
    image, keypoints, None, (0, 0, 255),
    cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)
cv2.imshow("Blob Detection", blob_image)
cv2.imwrite(out("blobs.jpg"), blob_image)

print("Contours detected:", len(contours))
print("Blobs detected:", len(keypoints))
print("Processed images saved next to this script.")
print("Press any key on an image window to close all windows.")

cv2.waitKey(0)
cv2.destroyAllWindows()
