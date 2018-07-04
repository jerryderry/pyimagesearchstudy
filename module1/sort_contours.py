import numpy as np
import cv2
import argparse

def sort_contours(contours, method="left-to-right"):
    # initialize the reverse flag and sort index
    reverse = False
    i = 0

    # handle if we need to sort in reverse
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True

    # handle if we are sorting against the y coordinate rather than
    # the x coordinate of the bounding box
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1

    # construct the list of bounding boxes and sort them from top to bottom
    bounding_boxes = [cv2.boundingRect(c) for c in contours]
    (contours, bounding_boxes) = zip(*sorted(zip(contours, bounding_boxes),
                                             key=lambda b: b[1][i],
                                             reverse=reverse))

    # return the list of sorted contours and bounding boxes
    return (contours, bounding_boxes)


def draw_contour(image, contour, contour_index):
    # compute the center of the contour, and draw a circle
    # representing the center
    moments = cv2.moments(contour)
    center_x = int(moments["m10"] / moments["m00"])
    center_y = int(moments["m01"] / moments["m00"])

    # draw the contour number on the image
    cv2.putText(image, "#{}".format(contour_index+1),
                org=(center_x-20, center_y),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                fontScale=1.0,
                color=(255, 255, 255),
                thickness=2)
    return image


# construct the argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the input image")
arg_parser.add_argument("-m", "--method", required=True, help="Sorting method")
args = vars(arg_parser.parse_args())

# load the image and initialize the accumulated edge image
img = cv2.imread(args["image"])
accum_edge = np.zeros(img.shape[0:2], dtype=np.uint8)

# loop over the blue, green and red channels, respectively
for channel in cv2.split(img):
    # blur the channel, extract edges from it, and accumulate the set
    # of edges for the image
    channel = cv2.medianBlur(channel, ksize=11)
    edged = cv2.Canny(channel, 50, 200)
    accum_edge = cv2.bitwise_or(accum_edge, edged)

# show the accumulated edge map
cv2.imshow("Edge Map", accum_edge)

# find contours in the accumulated image, keeping only the largest ones
(_, contours, _) = cv2.findContours(accum_edge.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
original = img.copy()

# loop over the contours and draw them
for (i, c) in enumerate(contours):
    original = draw_contour(original, c, i)

# show the original, unsorted contour image
cv2.imshow("Unsorted", original)

# sort the contours according to the provided method
(contours, bounding_boxes) = sort_contours(contours, method=args["method"])

# loop over the sorted contours and draw them
for (i, c) in enumerate(contours):
    draw_contour(img, c, i)

# show the output image
cv2.imshow("Sorted", img)
cv2.waitKey(0)
