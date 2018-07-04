import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert it to grayscale
img = cv2.imread(args["image"])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# apply histogram equalization to stretch the contrast of our image
eq = cv2.equalizeHist(img)

# show the images
cv2.imshow("Original", img)
cv2.imshow("Histogram Equalization", eq)
cv2.waitKey(0)
