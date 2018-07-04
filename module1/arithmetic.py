import numpy as np
import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and show it
img = cv2.imread(args["image"])
cv2.imshow("Original", img)
cv2.waitKey(0)

print("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8([100])))))
print("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))

print("wrap around: {}".format(str(np.uint8(200) + np.uint8(100))))
print("wrap around: {}".format(str(np.uint8(50) - np.uint8(100))))

M = np.ones(img.shape, dtype=np.uint8) * 100
added = cv2.add(img, M)
cv2.imshow("Added", added)

M = np.ones(img.shape, dtype=np.uint8) * 50
subtracted = cv2.subtract(img, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)

M = np.ones(img.shape, dtype=np.uint8) * 75
added = cv2.add(img, M)
print(added[152, 61])
