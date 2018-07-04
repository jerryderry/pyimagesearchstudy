from skimage.filters import threshold_local
import cv2
import argparse
import numpy as np

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale and blur it slightly
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Blur", blur)

# apply adaptive thresholding with OpenCV
neighbourhood_size = 25
constant_c = 15
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV,
                               neighbourhood_size, constant_c)
cv2.imshow("OpenCV Mean Threshold", thresh)

# apply adaptive thresholding with scikit-image
neighbourhood_size = 29
constant_c = 5
threshold_value = threshold_local(blur, neighbourhood_size, offset=constant_c)
thresh = (blur < threshold_value).astype(np.uint8) * 255
cv2.imshow("Scikit-image Mean Threshold", thresh)
cv2.waitKey(0)
