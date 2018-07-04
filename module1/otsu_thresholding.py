import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale and blur it slightly
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow("Blur", blur)

# apply Otsu's automatic thresholding
(threshold_value, thresh_inv) = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("Threshold", thresh_inv)
print("Otsu's threshold value is {}".format(threshold_value))

# visualize the masked region
cv2.imshow("Output", cv2.bitwise_and(img, img, mask=thresh_inv))
cv2.waitKey(0)
