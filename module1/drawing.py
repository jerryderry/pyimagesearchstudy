import numpy as np
import cv2

canvas = np.zeros((300, 300, 3), dtype=np.uint8)

# draw a green line from top left to bottom right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a 3-pixel thick red line from top right to bottom left
red = (0, 0, 255)
cv2.line(canvas, (0, 300), (300, 0), red, thickness=3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a green rectangle starting at (10, 10) and ending at (60, 60)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a red rectangle with 5 pixel thickness
cv2.rectangle(canvas, (50, 200), (200, 225), red, thickness=5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a filled blue rectangle, give thickness a negative value
blue = (225, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, thickness=-1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# reset canvas and draw white circles at the center with increasing radii
# from 25 pixels to 150 pixels
canvas = np.zeros((300, 300, 3), dtype=np.uint8)
center_x, center_y = canvas.shape[1] // 2, canvas.shape[0] // 2
white = (255, 255, 255)

# stepping 25 pixels
for radius in range(25, 175, 25):
    cv2.circle(canvas, (center_y, center_x), radius, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw 25 random circles
for _ in range(25):
    radius = np.random.randint(0, high=200)
    color = tuple(np.random.randint(0, high=256, size=(3,))) # can't give it type of "uint8"
    center = tuple(np.random.randint(0, high=300, size=(2,)))

    cv2.circle(canvas, center, radius, color, thickness=-1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

