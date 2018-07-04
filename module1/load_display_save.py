# import the necessary packages
import cv2
import argparse

# construct the argument parser and parse the arguments
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
arg_parser.add_argument("-s", "--save", required=False, help="Path to the new saved image")
# argument value dict
args = vars(arg_parser.parse_args())

# load the image
image = cv2.imread(args["image"])
print("width: {} pixels".format(image.shape[1]))
print("height: {} pixels".format(image.shape[0]))
print("channels: {}".format(image.shape[2]))

# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)  # any key

# save the image
if args["save"]:
    cv2.imwrite(args["save"], image)
