# import the necessary packages
import cv2
import argparse

# construct the argument parser and parse the arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
# argParser.add_argument("-s", "--save", required=False, help="Path to the new saved image")
# argument value dict
args = vars(arg_parser.parse_args())

# load the image, grab the dimensions and show the image
image = cv2.imread(args["image"])
(height, width) = image.shape[0:2]
cv2.imshow("Original", image)
cv2.waitKey(0)

# Pixel at (0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# Change (0, 0) to red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[225, 111]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

# Grab top left part of the image
center_x, center_y = width // 2, height // 2
topLeft = image[0:center_y, 0:center_x]
cv2.imshow("Top-left corner", topLeft)
cv2.waitKey(0)
