import cv2
import argparse

from module1 import imbasics

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale and blur it slightly
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
cv2.imshow("Original", img)
cv2.imshow("Blurred", blur)

# compute a "wide", "mid-range" and "tight" threshold for the edge
wide = cv2.Canny(blur, 10, 200)
mid = cv2.Canny(blur, 30, 150)
tight = cv2.Canny(blur, 240, 250)
auto = imbasics.auto_canny(blur)

cv2.imshow("Wide Edge Map", wide)
cv2.imshow("Mid Edge Map", mid)
cv2.imshow("Tight Edge Map", tight)
cv2.imshow("Auto Edge Map", auto)
cv2.waitKey(0)
