import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image
img = cv2.imread(args["image"])
cv2.imshow("Original", img)
cv2.waitKey(0)

# initialize a list of kernel sizes
kernel_sizes = [(3, 3), (9, 9), (15, 15)]

# ----------- Average blur ---------------
#
# loop over the sizes and apply an average blur
for (size_y, size_x) in kernel_sizes:
    blurred = cv2.blur(img, (size_x, size_y))
    cv2.imshow("Average: ({}, {})".format(size_y, size_x), blurred)
    cv2.waitKey(0)

# close all windows and clean up the screen
cv2.destroyAllWindows()

# ----------- Gaussian blur --------------
#
# loop over the sizes and apply a Gaussian blur
for (size_y, size_x) in kernel_sizes:
    blurred = cv2.GaussianBlur(img, (size_x, size_y), 0)
    cv2.imshow("Gaussian: ({}, {})".format(size_y, size_x), blurred)
    cv2.waitKey(0)

# close all windows and clean up the screen
cv2.destroyAllWindows()

# ------------ Median blur ---------------
#
# loop over the sizes and apply a median blur
for (size, _) in kernel_sizes:
    blurred = cv2.medianBlur(img, size)
    cv2.imshow("Median: ({}, {})".format(size, size), blurred)
    cv2.waitKey(0)
