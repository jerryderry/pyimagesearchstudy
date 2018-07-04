import cv2

# load the receipt image, convert it to grayscale, and detect edges
img = cv2.imread("receipt.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(gray, 75, 200)

# show the original image and edged map
cv2.imshow("Original", img)
cv2.imshow("Edge Map", edged)

# find contours in the image and sort them from largest to smallest,
# keeping only the largest ones
(_, contours, _) = cv2.findContours(edged, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[0:7]

# loop over the contours
for c in contours:
    # approximate the contour
    perimeter = cv2.arcLength(c, closed=True)
    approx = cv2.approxPolyDP(c, epsilon=0.01*perimeter, closed=True)

    # show the difference in number of vertices between the original
    # and approximated contours
    print("original: {}, approx: {}".format(len(c), len(approx)))

    # if the approximated contour has 4 vertices, then we have found our rectangle
    if len(approx) == 4:
        # draw the outline on the image
        cv2.drawContours(img, [approx], contourIdx=-1, color=(0, 255, 0), thickness=2)

# show the output image
cv2.imshow("Output", img)
cv2.waitKey(0)
