import cv2
import numpy as np

# load the Tetris block image, convert it to grayscale, and threshold the image
img = cv2.imread("tetris_blocks.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(_, thresh) = cv2.threshold(gray, thresh=225, maxval=255, type=cv2.THRESH_BINARY_INV)

# show the image and thresholded image
cv2.imshow("Original", img)
cv2.imshow("Thresholded", thresh)

# find the external contours in the thresholded image
(_, contours, _) = cv2.findContours(thresh, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

# allocate memory for the convex hull image
hull_img = np.zeros(gray.shape[0:2], dtype=np.uint8)

# loop over the contours
for (i, c) in enumerate(contours):
    # compute area of the contour
    area = cv2.contourArea(c)

    # compute aspect ratio of the contour
    (x, y, width, height) = cv2.boundingRect(c)
    aspect_ratio = width / height

    # compute extent
    extent = area / (width * height)

    # compute the convex hull of the contour and its solidity
    hull = cv2.convexHull(c)
    hull_area = cv2.contourArea(hull)
    solidity = area / hull_area

    # visualize the original contours and the convex hull
    cv2.drawContours(hull_img, [hull], contourIdx=-1, color=255, thickness=-1)
    cv2.drawContours(img, [c], contourIdx=-1, color=(240, 0, 159), thickness=3)

    shape = ""

    # if the aspect ratio is approximately 1, then it is a square
    if aspect_ratio >= 0.98 and aspect_ratio <= 1.02:
        shape = "SQUARE"

    # if the width is 3 times of the height, it is a rectangle
    elif aspect_ratio >= 3.0:
        shape = "RECTANGLE"

    # if the extent is sufficiently small, it is an L-shape
    elif extent < 0.65:
        shape = "L-PIECE"

    # if the solidity is sufficiently large enough, it is a Z-piece
    elif solidity > 0.80:
        shape = "Z-PIECE"

    # draw the shape name on the image
    cv2.putText(img, shape,
                org=(x, y-10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=0.5,
                color=(240, 0, 159),
                thickness=2)

    print("Contour #{} -- aspect ratio={:.2f}, extent={:.2f}, solidity={:.2f}".format(i+1, aspect_ratio, extent, solidity))

    # show the outputs
    cv2.imshow("Convex Hull", hull_img)
    cv2.imshow("Image", img)
    cv2.waitKey(0)

