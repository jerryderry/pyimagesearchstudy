from matplotlib import pyplot as plt
import cv2
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_args())

# load the image, convert it to grayscale and show it
img = cv2.imread(args["image"])
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Orginal", img)
cv2.waitKey(0)

# construct a grayscale histogram
hist = cv2.calcHist([img], channels=[0], mask=None, histSize=[256], ranges=[0, 256])

# plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])

# normalize the histogram
hist /= hist.sum()

# plot the normalized histogram
plt.figure()
plt.title("Grayscale Histogram (Normalized)")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
