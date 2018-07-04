from matplotlib import pyplot as plt
import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image and show it
img = cv2.imread(args["image"])
cv2.imshow("Orginal", img)
cv2.waitKey(0)

# grab the image channels, initialize the tuple of colors and the figure
channels = cv2.split(img)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# loop over the image channels
for (channel, color) in zip(channels, colors):
    # create a histogram for the current channel and plot it
    hist = cv2.calcHist([channel], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.show()

# ------------- 2D Histogram ----------------
#
# reduce the number of bins from 256 to 32
fig = plt.figure()

# plot a 2D histogram for green and blue
ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]],
                    channels=[0, 1],
                    mask=None,
                    histSize=[32, 32],
                    ranges=[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

# plot a 2D histogram for green and red
ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]],
                    channels=[0, 1],
                    mask=None,
                    histSize=[32, 32],
                    ranges=[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

# plot a 2D histogram for blue and red
ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]],
                    channels=[0, 1],
                    mask=None,
                    histSize=[32, 32],
                    ranges=[0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)
plt.show()

# the dimensionality of one of the 2D histograms
print("2D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

# ----------- 3D Histogram -----------------
#
# 8 bins in each direction
hist = cv2.calcHist([img], channels=[0, 1, 2],
                    mask=None,
                    histSize=[8, 8, 8],
                    ranges=[0, 256, 0, 256, 0, 256])
print("3D histogram shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))