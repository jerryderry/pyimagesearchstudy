import numpy as np
import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

img = cv2.imread(args["image"])
cv2.imshow("Original", img)
cv2.waitKey(0)

mask = np.zeros(img.shape[0:2], dtype=np.uint8)
cv2.rectangle(mask, (0, 90), (290, 450), 255, thickness=-1)
cv2.imshow("Mask", mask)

# apply the mask
masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# apply a circular mask
mask = np.zeros(img.shape[0:2], dtype=np.uint8)
cv2.circle(mask, (145, 200), 100, 255, thickness=-1)
cv2.imshow("Mask", mask)
masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
