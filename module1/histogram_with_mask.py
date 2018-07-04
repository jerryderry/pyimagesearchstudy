from matplotlib import pyplot as plt
import numpy as np
import cv2

def plot_histogram(image, title, mask=None):
    # grab the image channels, initialize the tuple of colors and the figure
    channels = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    # loop over the image channels
    for (channel, color) in zip(channels, colors):
        # create a histogram for the current channel and plot it
        hist = cv2.calcHist([channel],
                            channels=[0],
                            mask=mask,
                            histSize=[256],
                            ranges=[0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])

# load the image and plot a histogram for it
image = cv2.imread("giraffe.png")
cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")

# construct a mask
mask = np.zeros(image.shape[0:2], dtype=np.uint8)
cv2.rectangle(mask, (60, 290), (210, 390), color=255, thickness=-1)
cv2.imshow("Mask", mask)

masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the Mask", masked)

# compute a histogram for the image but only include pixels in the masked region
plot_histogram(image, "Histogram for Masked Image", mask=mask)
plt.show()
