import numpy as np
import argparse
from module1 import imbasics
import cv2

# construct the argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image
img = cv2.imread(args["image"])
cv2.imshow("Image", img)
cv2.waitKey(0)

# translation matrix
# | 1 0 pixelsToTranslateInX |
# | 1 0 pixelsToTranslateInY |
# translate image 25 pixels to the right and 50 pixels down
M = np.array([[1, 0, 25], [0, 1, 50]], dtype=np.float32)
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted down and right", shifted)
cv2.waitKey(0)

# shift the image 50 pixels to the right and 90 pixels up
M = np.array([[1, 0, -50], [0, 1, -90]], dtype=np.float32)
shifted = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
cv2.imshow("Shifted left and up", shifted)
cv2.waitKey(0)

# shift the image down 100 pixels
shifted = imbasics.translate(img, 0, 100)
cv2.imshow("Shifted down", shifted)
cv2.waitKey(0)


