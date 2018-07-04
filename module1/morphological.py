import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and convert to grayscale
img = cv2.imread(args["image"])
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", gray)
cv2.waitKey(0)

# apply a series of erosions
for i in range(3):
    eroded = cv2.erode(gray.copy(), None, iterations=i+1)
    cv2.imshow("Eroded {} times".format(i+1), eroded)
    cv2.waitKey(0)

# close all windows and clean up the screen
cv2.destroyAllWindows()
cv2.imshow("Original", gray)

# apply a series of dilations
for i in range(3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i+1)
    cv2.imshow("Dilated {} times".format(i+1), dilated)
    cv2.waitKey(0)

# close all windows and clean up the screen
cv2.destroyAllWindows()
# initialize a list of kernel sizes
kernel_sizes = [(3, 3), (5, 5), (7, 7)]

# loop over the kernels and apply an opening operation
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(kernel_size[0], kernel_size[1]), opening)
    cv2.waitKey(0)

# close all windows and clean up the screen
cv2.destroyAllWindows()

# loop over the kernels and apply a closing operation
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closing: ({}, {})".format(kernel_size[0], kernel_size[1]), closing)
    cv2.waitKey(0)

# close all windows and clean up the screen
cv2.destroyAllWindows()

# loop over the kernels and apply a morphological gradient operation
for kernel_size in kernel_sizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)
    gradient = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
    cv2.imshow("Gradient: ({}, {})".format(kernel_size[0], kernel_size[1]), gradient)
    cv2.waitKey(0)
