import cv2
import argparse
import numpy as np

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)

# find all contours in the image and draw all contours on the image
# for OpenCV 3, the returned tuple is (image, contours, contour hierarchy)
(_, contours, _) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
clone = img.copy()
cv2.drawContours(clone, contours, contourIdx=-1, color=(0, 255, 0), thickness=2)
print("Found {} contours.".format(len(contours)))

cv2.imshow("All Contours", clone)
cv2.waitKey(0)

# re-clone the image and close all windows
clone = img.copy()
cv2.destroyAllWindows()

# loop over the contours individually and draw each of them
for (i, c) in enumerate(contours):
    print("Drawing contour #{}".format(i+1))
    cv2.drawContours(clone, [c], contourIdx=-1, color=(0, 255, 0), thickness=2)
    cv2.imshow("Single Contour", clone)
    cv2.waitKey(0)

# re-clone the image and close all windows
clone = img.copy()
cv2.destroyAllWindows()

# find external contours
(_, contours, _) = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(clone, contours, contourIdx=-1, color=(0, 255, 0), thickness=2)
cv2.imshow("All Contours", clone)
cv2.waitKey(0)

# re-clone the image and close all windows
clone = img.copy()
cv2.destroyAllWindows()

# loop over the contours and apply masks
for c in contours:
    mask = np.zeros(gray.shape, dtype=np.uint8)
    cv2.drawContours(mask, [c], contourIdx=-1, color=255, thickness=-1)

    cv2.imshow("Image + Mask", cv2.bitwise_and(img, img, mask=mask))
    cv2.waitKey(0)
