import numpy as np
import cv2

# draw a rectangle
rectangle_canvas = np.zeros((300, 300), dtype=np.uint8)
cv2.rectangle(rectangle_canvas, (25, 25), (275, 275), 255, thickness=-1)
cv2.imshow("Rectangle", rectangle_canvas)

# draw a circle
circle_canvas = np.zeros((300, 300), dtype=np.uint8)
cv2.circle(circle_canvas, (150, 150), 150, 255, thickness=-1)
cv2.imshow("Circle", circle_canvas)
cv2.waitKey(0)

# bitwise AND
bitwise_and = cv2.bitwise_and(rectangle_canvas, circle_canvas)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.waitKey(0)

# bitwise OR
bitwise_or = cv2.bitwise_or(rectangle_canvas, circle_canvas)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.waitKey(0)

# bitwise XOR
bitwise_xor = cv2.bitwise_xor(rectangle_canvas, circle_canvas)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.waitKey(0)

# bitwise NOT
bitwise_not = cv2.bitwise_not(circle_canvas)
cv2.imshow("Bitwise NOT", bitwise_not)
cv2.waitKey(0)
