import cv2

# load the tic-tac-toe image and convert it to grayscale
img = cv2.imread("tictactoe.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find all contours on the tic-tac-toe board
(_, contours, _) = cv2.findContours(gray, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

# loop over the contours
for (i, c) in enumerate(contours):
    # compute the area of the contour
    area = cv2.contourArea(c)
    # compute the bounding box
    (x, y, width, height) = cv2.boundingRect(c)

    # compute the convex hull of the contour
    hull = cv2.convexHull(c)
    # compute the area of the convex hull to get solidity
    hull_area = cv2.contourArea(hull)
    solidity = area / float(hull_area)

    # initialize the character text
    char = "?"

    # if the solidity is high, then we are examining an "O"
    if solidity > 0.9:
        char = "O"
    elif solidity > 0.5:
        char = "X"

    # if the character is known, draw it
    if char != "?":
        cv2.drawContours(img, [c], contourIdx=-1, color=(0, 255, 0), thickness=3)
        cv2.putText(img, char,
                    org=(x, y-10),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1.25,
                    color=(0, 255, 0),
                    thickness=4)

    print("{} (Contour #{}) -- solidity={:.2f}".format(char, i+1, solidity))

cv2.imshow("Output", img)
cv2.waitKey(0)
