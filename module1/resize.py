import cv2
import argparse

from module1 import imbasics

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and show it
img = cv2.imread(args["image"])
cv2.imshow("Original", img)
cv2.waitKey(0)

# resize to 150 pixels wide
aspect_ratio = img.shape[1] / img.shape[0]
resized_height = int(150.0 / aspect_ratio)

resized = cv2.resize(img, (150, resized_height), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.waitKey(0)

# resize original image to 50 pixels tall
resized_width = int(aspect_ratio * 50)
resized = cv2.resize(img, (resized_width, 50), interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.waitKey(0)

# resize image to 50 pixels tall using function
resized = imbasics.resize(img, height=50)
cv2.imshow("Resized", resized)
cv2.waitKey(0)

# different interpolation methods
methods = [("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
           ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
           ("cv2.INTER_AREA", cv2.INTER_AREA),
           ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
           ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]

for (name, method) in methods:
    # magnify the image to 3 times
    resized = imbasics.resize(img, width=img.shape[1] * 3, interpolation=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)


