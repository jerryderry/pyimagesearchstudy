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

# dimensions and center of the image
(height, width) = img.shape[0:2]
center_x, center_y = width // 2, height // 2

# rotate image by 45 degrees
R = cv2.getRotationMatrix2D((center_x, center_y), 45, 1.0)
rotated = cv2.warpAffine(img, R, (width, height))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.waitKey(0)

# rotate image by -90 degrees
R = cv2.getRotationMatrix2D((center_x, center_y), -90, 1.0)
rotated = cv2.warpAffine(img, R, (width, height))
cv2.imshow("Rotated by -90 Degrees", rotated)
cv2.waitKey(0)

# rotate about an arbitrary point
R = cv2.getRotationMatrix2D((center_x - 50, center_y - 50), 45, 1.0)
rotated = cv2.warpAffine(img, R, (width, height))
cv2.imshow("Rotated by offset & 45 degrees", rotated)
cv2.waitKey(0)

# rotate image 180 degrees
rotated = imbasics.rotate(img, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)
