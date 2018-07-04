import cv2
import argparse
import numpy as np

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
arg_parser.add_argument("-l", "--lower_angle", type=float, default=175.0,
                        help="Lower orientation angle")
arg_parser.add_argument("-u", "--upper_angle", type=float, default=180.0,
                        help="Upper orientation angle")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", gray)

# compute gradients along x and y axis, respectively
g_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
g_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

# compute the gradient magnitude and orientation
magnitude = np.sqrt(g_x ** 2 + g_y ** 2)
orientation = np.arctan2(g_y, g_x) * 180 / np.pi

# find all pixels that are within the lower and upper angle boundaries
indices = np.where(orientation >= args["lower_angle"], orientation, -1)
indices = np.where(orientation <= args["upper_angle"], indices, -1)
mask = np.zeros(gray.shape, dtype=np.uint8)
mask[indices > -1] = 255

# show the image
cv2.imshow("Mask", mask)
cv2.waitKey(0)
