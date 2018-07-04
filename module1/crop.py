import cv2
# import argparse
#
# arg_parser = argparse.ArgumentParser()
# arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
# args = vars(arg_parser.parse_args())

# load the image and show it
# img = cv2.imread(args["image"])
img = cv2.imread("florida_trip.png")
cv2.imshow("Original", img)
cv2.waitKey(0)

face = img[85:250, 85:220]
cv2.imshow("Face", face)
cv2.waitKey(0)

body = img[90:450, 0:290]
cv2.imshow("Body", body)
cv2.waitKey(0)

people = img[173:235, 13:81]
cv2.imshow("People", people)
cv2.waitKey(0)
