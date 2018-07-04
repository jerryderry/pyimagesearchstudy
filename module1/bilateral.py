import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image
img = cv2.imread(args["image"])
cv2.imshow("Original", img)
cv2.waitKey(0)

# construct a list of bilateral filter parameters
params = [(11, 21, 7), (11, 41, 21), (11, 61, 39)]

# loop over the diameter, sigma color and sigma space
for (diameter, sigma_color, sigma_space) in params:
    blurred = cv2.bilateralFilter(img, diameter, sigma_color, sigma_space)
    title = "Blurred: d={}, sc={}, ss={}".format(diameter, sigma_color, sigma_space)
    cv2.imshow(title, blurred)
    cv2.waitKey(0)
