import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image
img = cv2.imread(args["image"])
cv2.imshow("RGB", img)

# loop over each of the channels and display them
for (name, channel) in zip(("B", "G", "R"), cv2.split(img)):
    cv2.imshow(name, channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ----------- HSV ----------------
#
# convert the image to the HSV color space and show it
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV", hsv)

# loop over each of the channels and display them
for (name, channel) in zip(("H", "S", "V"), cv2.split(hsv)):
    cv2.imshow(name, channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ----------- L*a*b ---------------
#
# convert the image to the L*a*b color space and show it
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow("L*a*b", lab)

# loop over each of the channels and display them
for (name, channel) in zip(("L", "*a", "*b"), cv2.split(lab)):
    cv2.imshow(name, channel)

cv2.waitKey(0)
cv2.destroyAllWindows()

# ----------- Grayscale -------------
#
# convert the image to the grayscale and show it
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
