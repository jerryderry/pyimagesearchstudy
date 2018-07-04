import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale and blur it slightly
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", gray)

# compute gradients along the x and y axis, respectively
g_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
g_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)

# convert from float to uint8
g_x = cv2.convertScaleAbs(g_x)
g_y = cv2.convertScaleAbs(g_y)

# combine the sobel x and y representations into one image
sobel_combined = cv2.addWeighted(g_x, 0.5, g_y, 0.5, 0)

# show the images
cv2.imshow("Sobel X", g_x)
cv2.imshow("Sobel Y", g_y)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.waitKey(0)
