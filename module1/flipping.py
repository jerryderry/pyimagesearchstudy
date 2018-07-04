import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and show it
img = cv2.imread(args["image"])
cv2.imshow("Original", img)
cv2.waitKey(0)

# flip the image horizontally
flipped = cv2.flip(img, 1)
cv2.imshow("Flipped horizontally", flipped)
cv2.waitKey(0)

# flip the image vertically
flipped = cv2.flip(img, 0)
cv2.imshow("Flipped vertically", flipped)
cv2.waitKey(0)

