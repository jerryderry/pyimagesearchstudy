import numpy as np
import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and grab each channel
img = cv2.imread(args["image"])
(blue_channel, green_channel, red_channel) = cv2.split(img)


# show each channel
cv2.imshow("Red", red_channel)
cv2.imshow("Green", green_channel)
cv2.imshow("Blue", blue_channel)
cv2.waitKey(0)

# merge the image back
merged = cv2.merge([blue_channel, green_channel, red_channel])
cv2.imshow("Merged", merged)
cv2.waitKey(0)

# visualize each channel in color
zeros = np.zeros(img.shape[0:2], dtype=np.uint8)
cv2.imshow("Red", cv2.merge([zeros, zeros, red_channel]))
cv2.imshow("Green", cv2.merge([zeros, green_channel, zeros]))
cv2.imshow("Blue", cv2.merge([blue_channel, zeros, zeros]))
cv2.waitKey(0)


