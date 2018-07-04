from skimage.filters import threshold_local
from skimage import measure
import numpy as np
import cv2

# load the license plate image
plate = cv2.imread("license_plate.png")

# extract the Value component from the HSV color space and apply adaptive
# thresholding to reveal the characters on the license plate
value = cv2.split(cv2.cvtColor(plate, cv2.COLOR_BGR2HSV))[2]
threshold = threshold_local(value, block_size=29, offset=15)
thresh_img: np.ndarray = np.less(value, threshold).astype(np.uint8) * 255

# show the image
cv2.imshow("License Plate", plate)
cv2.imshow("Thresh", thresh_img)
cv2.waitKey(0)

# perform connected components analysis on the thresholded images
# and initialize the mask to hold only the "large" components
labels: np.ndarray = measure.label(thresh_img, neighbors=8, background=0)
mask = np.zeros(thresh_img.shape, dtype=np.uint8)
print("[INFO] found {} blobs".format(len(np.unique(labels))))

# loop over the unique components
for (i, label) in enumerate(np.unique(labels)):
    # if this is the background label, ignore it
    if label == 0:
        print("[INFO] label: 0 (background)")
        continue

    # otherwise, construct the label mask to display only connected
    # components for the current label
    print("[INFO] label: {} (foreground)".format(i))
    label_mask = np.zeros(thresh_img.shape, dtype=np.uint8)
    label_mask[labels == label] = 255
    num_pixels = cv2.countNonZero(label_mask)

    # if the number of pixels in the component is sufficiently large,
    # add it to our mask of "large" blobs
    if 300 < num_pixels < 1500:
        mask = cv2.add(mask, label_mask)

    # show the label mask
    cv2.imshow("Label", label_mask)
    cv2.waitKey(0)

# show the large components in the image
cv2.imshow("Large Blobs", mask)
cv2.waitKey(0)
