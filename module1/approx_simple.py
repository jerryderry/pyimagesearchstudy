import cv2

# load the circles and squares images and convert it to grayscale
img = cv2.imread("circles_and_squares.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find contours in the image
(_, contours, _) = cv2.findContours(gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for c in contours:
    # approximate the contour
    perimeter = cv2.arcLength(c, closed=True)
    approx = cv2.approxPolyDP(c, epsilon=0.01*perimeter, closed=True)

    # if the approximated contour has 4 vertices, then we are examining a rectangle
    if len(approx) == 4:
        # draw the outline of the contour and draw the text on the image
        cv2.drawContours(img, [c], contourIdx=-1, color=(0, 255, 255), thickness=2)
        (x, y, _, _) = cv2.boundingRect(c)
        cv2.putText(img, "Rectangle",
                    org=(x, y-10),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.5,
                    color=(0, 255, 255),
                    thickness=2)

# show the output image
cv2.imshow("Image", img)
cv2.waitKey(0)
