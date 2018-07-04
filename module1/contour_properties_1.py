import cv2
import argparse
import numpy as np

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find external contours
(_, contours, _) = cv2.findContours(gray.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
clone = img.copy()

# --------------- Centroid ----------------------
#
# loop over the contours
for c in contours:
    # compute the moments of the contour which can be used to compute
    # the centroid of the region
    moments = cv2.moments(c)   # a dictionary
    center_x = int(moments["m10"] / moments["m00"])
    center_y = int(moments["m01"] / moments["m00"])

    # draw the center of the contour on the image
    cv2.circle(clone, (center_x, center_y), 10, (0, 255, 0), thickness=-1)

# show the output image
cv2.imshow("Centroids", clone)
cv2.waitKey(0)

# --------------- Area and Perimeter --------------
#
# loop over the contours
for (i, c) in enumerate(contours):
    # compute the area and the perimeter
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, closed=True)
    print("Contour #{} -- area: {:.2f}, perimeter: {:.2f}".format(i+1, area, perimeter))

    # draw the contour on the image
    cv2.drawContours(clone, [c], contourIdx=-1, color=(0, 255, 0), thickness=2)

    # computer the center of the contour and draw the contour number
    moments = cv2.moments(c)
    center_x = int(moments["m10"] / moments["m00"])
    center_y = int(moments["m01"] / moments["m00"])
    cv2.putText(clone, "#{}".format(i+1),
                org=(center_x-20, center_y),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.25,
                color=(255, 255, 255),
                thickness=4)

# show the output image
cv2.imshow("Contours", clone)
cv2.waitKey(0)

# ---------------- Bounding Box -----------------
#
# clone the image
clone = img.copy()

# loop over the contours
for c in contours:
    # fit a bounding box to the contour
    (x, y, width, height) = cv2.boundingRect(c)
    cv2.rectangle(clone, pt1=(x, y), pt2=(x+width, y+height),
                  color=(0, 255, 0), thickness=2)

# show the output image
cv2.imshow("Bounding Boxes", clone)
cv2.waitKey(0)

# ---------------- Rotated Bounding Box -------------
#
# clone the image
clone = img.copy()
# loop over the contours
for c in contours:
    # fit a rotated bounding box to the contour
    # the method returns a tuple ((x, y), (width, height), angle)
    box = cv2.minAreaRect(c)
    # numpy.int0 is an alias of numpy.intp, which is a type for indexing.
    # It is equivalent to C's ssize_t, either int32 or int64
    box = np.int0(cv2.boxPoints(box))
    cv2.drawContours(clone, [box], contourIdx=-1, color=(0, 255, 0), thickness=2)

# show the output image
cv2.imshow("Rotated Bounding Box", clone)
cv2.waitKey(0)

# ---------------- Minimum Enclosing Circle ------------
#
# clone the image
clone = img.copy()
# loop over the contours
for c in contours:
    # fit a minimum enclosing circle to the contour
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(clone, (int(x), int(y)), int(radius), color=(0, 255, 0), thickness=2)

# show the output image
cv2.imshow("Min-Enclosing Circles", clone)
cv2.waitKey(0)

# ------------- Fitting an Ellipse ----------------
#
# clone the image
clone = img.copy()
# loop over the contours
for c in contours:
    # to fit an ellipse, our contour must have at least 5 points
    if len(c) >= 5:
        # fit an ellipse to the contour
        ellipse = cv2.fitEllipse(c)
        cv2.ellipse(clone, ellipse, color=(0, 255, 0), thickness=2)

# show the output image
cv2.imshow("Ellipses", clone)
cv2.waitKey(0)
