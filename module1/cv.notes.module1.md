# 1.1 Loading, displaying and saving images
## argument parser
```python
import argparse

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(arg_parser.parse_arg())  # vars returns a dictionary
                                     # mapping arguments and values
```

## other
`cv2.imread`, `cv2.imshow`, `cv2.imwrite`.

# 1.2 Image basics
Use a tuple to construct a RGB color.
Upper left corner is the origin. y axis points downwards.
To get the width and height of an image:
`(height, width) = image.shape[:2]`
OpenCV stores in the order BGR.
To get pixel values, just use Numpy indexing.

# 1.3 Drawing
## Line
```python
cv2.line(image_to_draw_on, (starting_x, starting_y), (ending_x, ending_y), color=tuple_of_color_value)
```
## Rectangle
```python
cv2.rectangle(image_to_draw_on,
              (upper_left_x, upper_left_y),
              (lower_right_x, lower_right_y),
              color=tuple_of_color_value,
              thickness=line_thickness)
```
If `thickness` is negative, then the shape is filled.
## Circle
```python
cv2.circle(image_to_draw_on,
           (center_x, center_y),
           radius,
           color=tuple_of_color_value)
```

# 1.4 Basic image processing
## 1.4.1 Translation
Use a translation matrix:
$\left[\bm{M}\right] = \left[
    \begin{matrix}
    1 & 0 & t_x\\
    0 & 1 & t_y
    \end{matrix}
\right].$

How to do:
```python
M = np.array([[1, 0, 25], [0, 1, 50]], dtype=np.float32)
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```

## 1.4.2 Rotation
Modified rotation matrix:
$\left[\bm{M}\right] = \left[
    \begin{matrix}
    \alpha & \beta & (1-\alpha)\times c_x - \beta\times c_y\\
    -\beta & \alpha & \beta\times c_x + (1-\alpha)\times c_y
    \end{matrix}
\right],$
where $\alpha = \text{scale}\cdot\cos{\theta}$, $\beta = \text{scale}\cdot\sin{\theta}$, $c_x$ and $c_y$ are the rotation center coordinates.

How to do:
```python
M = cv2.getRotationMatrix2D((center_x, center_y), angle, scale)
rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
```

## 1.4.3 Resize
```python
resized = cv2.resize(image, (output_width, output_height), interpolation=cv2.INTER_AREA)
```

## 1.4.4 Flipping
For generating more data.
```python
flipped = cv2.flip(image, 1)  # flip horizontally
flipped = cv2.flip(image, 0)  # flip vertically
flipped = cv2.flip(image, -1) # flip both axes
```

## 1.4.5 Cropping
To select and extract the Region of Interest (ROI).
Can be done with Numpy slicing.

## 1.4.6 Image arithmetic
OpenCV saturated addition and subtraction of matrices.
```python
result = cv2.add(image1, image2)
result = cv2.sutract(image1, image2)
```

## 1.4.7 Bitwise operations
To extract non-rectangular ROIs. To construct masks.
Draw shapes on a binary image. First create a black image with `np.zeros`. Then draw shapes with color `255`.
```python
result = cv2.bitwise_and(image1, image2)
result = cv2.bitwise_or(image1, image2)
result = cv2.bitwise_xor(image1, image2)
result = cv2.bitwise_not(image1, image2)
```

## 1.4.8 Masking
Create a mask using a binary image.
When applying the mask to an image, use `cv2.bitwise_and` on the image itself and give the mask to the `mask` argument.
```python
masked = cv2.bitwise_and(image, image, mask=mask)
```

## 1.4.9 Splitting and merging channels
```python
(b, g, r) = cv2.split(image)
merged = cv2.merge([b, g, r])
```
To visualize a single channel with color, merge the channel image with zero matrices.
```python
zeros = np.zeros(image.shape[:2], dtype=np.uint8)
cv2.merge([zeros, zeros, r])
```

# 1.5 Kernels
Used for blurring, sharpening, edge detection, etc.

# 1.6 Morphological operations
Operates on grayscale images.
These operations destroy the original image, so need to make a copy.
## Erosion
A foreground pixel in the input image will be kept **only if ALL pixels** inside the structuring element are > 0. Otherwise, the pixels are set to 0.
Pixels near the boundary of an object will be discarded.
Most useful for removing small blobs from an image or disconnecting two connected components.
```python
eroded = cv2.erode(gray.copy(), None, iteration=num_operations)
```
`None` means the structuring element is a 3-by-3 8-neighborhood one.

## Dilation
Opposite of erosion.
A center pixel of the structuring element is set to white if **ANY** pixel in the structuring element is > 0.
Useful for joining broken parts of an image together.
```python
dilated = cv2.dilate(gray.copy(), None, iteration=num_operations)
```

## Opening
Erosion followed by a dilation.
To remove small blobs from an image.
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size_tupe)
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
```
`MORPH_RECT` with `(3, 3)` kernel size gives us an 8-neighborhood structuring element.

## Closing
Opposite of opening.
Dilation followed by a erosion.
Used to close holes inside of objects or for connecting components together.
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size_tupe)
opening = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)
```

## Morphological gradient
Difference between the dilation and erosion.
Useful for determining the outline of a particular object.
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size_tupe)
opening = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
```

## Top hat / white hat
Difference between the original and the opening.
Used to reveal **bright regions** on **dark backgrounds**.
```python
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size_tupe)
opening = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, kernel)
```
To apply it on a license plate, kernel size may be a rectangular one.

## Black hat
Difference between the closing and the original image.
Used to reveal dark regions against light backgrounds.

# 1.7 Smoothing and blurring
One of the most common pre-processing steps.
Thresholding and edge detection perform better if the image is first smoothed or blurred. We are able to reduce the amount of high frequency content, such as noise and edges.

## Averaging
The larger your smoothing kernel is, the more blurred your image will look.
```python
blurred = cv2.blur(image, (kernel_size_x, kernel_size_y))
```

## Gaussian
```python
blurred = cv2.GaussianBlur(image, (kernel_size_x, kernel_size_y), sigmaX=0)
```
If `sigmaX` is set to `0`, then `sigmaX` and `sigmaY` will be automatically calculated.

## Median
Most effective when removing salt-and-pepper noise.
Kernel size for median must be square.
```python
blurred = cv2.medianBlur(image, kernel_size)
```

## Bilateral
To reduce noise while still maintaining edges, we use bilateral blurring.
It uses to Gaussian distributions.
The first only considers spatial neighbors. The second considers pixel intensities. Only similar intensities will be blurred.
```python
blurred = cv2.bilateralFilter(image, diameter, sigma_color, sigma_space)
```

# 1.8 Lighting and color space
Lighting conditions should have three primary goals:
1. High Contrast
2. Generalizable
3. Stable

## Color space
1. RGB
2. HSV
3. L* a* b
4. Grayscale
When converting to grayscale, each channel is not weighted uniformly.
$Y = 0.299R + 0.587G + 0.114B$

# 1.9 Thresholding
To separate the foreground from the background.
Convert a grayscale image to a binary image.
Convert the image to grayscale and blur it first.

## Simple thresholding
```python
(threshold_value, threshed_img) = cv2.threshold(img, threshold_value, max_pixel_value, cv2.THRESH_BINARY_INV)
```
`THRESH_BINARY_INV` means pixel values larger than `threshold_value` will be set to 0, otherwise set to `max_pixel_value`.
The thresholded image can often be used as a mask.

## Otsu's method
Assumes the image contains two classes of pixels: background and foreground.
Assumes the grayscale histogram is bi-modal.
It is global thresholding.
```python
(threshold_value, threshed_img) = cv2.threshold(img, whatever_threshold_value, max_pixel_value, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
```
The threshold value given to `threshold` can be any number. It doesn't matter.

# Adaptive thresholding
Choosing the size of the pixel neighborhood for local thresholding is crucial.
Often use arithmetic mean or Gaussian mean to determine the threshold value in each region.
```python
threshed_img = cv2.adaptiveThreshold(img, max_pixel_value, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, neighborhood_size, a_constant_subtracted_from_mean)
```
We fine tune the hyperparameter `a_constant_subtracted_from_mean`.
We can also use `scikit-image`.
```python
threshed_img = skimage.filters.threshold_local(img, neighborhood_size, offset=a_constant, method="gaussian")
```

# 1.10 Gradients and edge detection
## 1.10.1 Gradients
Use gradients to detect edges, which lead to contours and outlines.
Used in Histogram of Oriented Gradients and SIFT.
Used to construct saliency maps.
Use kernels to calculate gradients.
### Sobel and Scharr kernels
Two kernels in each direction.
Used on grayscale images.
```python
# gradients along x axis
g_x = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=1, dy=0)
# gradients along y axis
g_y = cv2.Sobel(gray, ddepth=cv2.CV_64F, dx=0, dy=1)
```
If we want to visualize it, we need to change them from floating point to `uint8`.
```python
g_x = cv2.convertScaleAbs(g_x)
g_y = cv2.convertScaleAbs(g_y)
# combine them
sobel = cv2.addWeighted(g_x, 0.5, g_y, 0.5, 0)
```

## 1.10.2 Edge detection
An edge is defined to be a sharp difference and change in pixel values.
- Step edge
- Ramp edge
- Ridge edge
- Roof edge

### Canny edge detector
1. Apply Gaussian smoothing
2. Compute gradients in two directions with Sobel kernels
3. Non-maxima suppression (edge thinning)
   1. Compare the current pixel with its 3-by-3 neighborhood
   2. Determine the gradient orientation
   3. Compare the center pixel value with the pixels along the gradient vector direction. Preserve the larger value, discard the smaller ones.
4. Hysteresis thresholding
   1. Define $T_{upper}$ and $T_{lower}$
   2. Any gradient magnitude larger than $T_{upper}$ is an edge; any gradient magnitude smaller than $T_{lower}$ is not an edge; any gradient magnitude within the range:
      1. If it is connected to a strong edge, it is an edge.
      2. Otherwise, not an edge.

Although Canny edge detection contains Gaussian blur, we often still apply one before edge detection.

```python
edge_map = cv2.Canny(blurred, threshold_lower, threshold_upper)
```

We can calculate the median of the image, and use 1+0.33 times median to be the upper value, and 1-0.33 times median to be the lower value.

# 1.11 Contours
## 1.11.1 Finding and drawing contours
To actually find and access the result from thresholding or edge detection, we use contours.
If the image is simple enough, we might be able to find contours with just the grayscale image as inputs.
But for complicated images, we must first find the object by using thresholding or edge detection, which produces a binary image separating foreground and background.
Switching from grayscale to binary image will improve contour accuracy.

```python
(img, contours, hierarchies) = cv2.findContours(gray.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# drawing
cv2.drawContours(image, contours, -1, color=(0, 255, 0), thickness=2)
```
`findContours` will destroy the original image.
`RETR_LIST` means to get a list of all contours.
`-1` in `drawContours` means draw all contours in the list given.
To get only external contours, use `cv2.RETR_EXTERNAL`.

### Use contours and masks together
Draw the contour on a mask image, and then apply the mask with bitwise and.
```python
mask = np.zeros(gray.shape, dtype=np.uint8)
cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
img = cv2.bitwise_and(image, image, mask=mask)
```

## 1.11.2 Simple contour properties
### Centroid
```python
moments = cv2.moments(contour)
center_x = int(moments["m10"] / moments["m00"])
center_y = int(moments["m01"] / moments["m00"])
```

### Area and perimeter
```python
area = cv2.contourArea(contour)
perimeter = cv2.arcLength(contour, closed=True)
```

To draw text
```python
cv2.putText(image, "string", (x, y), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                                     fontScale=1.25,
                                     color=(255, 255, 255),
                                     thickness=4)
```

### Bounding boxes
Contains four components: upper left x and y coordinates and width and height of the box.
```python
(x, y, width, height) = cv2.boundingRect(contour)
```

To get a rotated bounding box:
```python
box = cv2.minAreaRect(contour)
box = np.int0(cv2.boxPoints(box))  # this is like a contour
```

### Minimum enclosing circle
```python
((x, y), radius) = cv2.minEnclosingCircle(contour)
```

### Ellipse
```python
ellipse = cv2.fitEllipse(contour)
```
To draw it, simply:
```python
cv2.ellipse(image, ellipse, color=(0, 255, 0), thickness=2)
```

## 1.11.3 Advanced contour properties
### Aspect ratio
aspect ratio = image width / image height
Use it to distinguish shapes.

### Extent
extent = shape area / bounding box area
It cannot be larger than 1.
When used to distinguish shapes, one needs to manually inspect the values of extent to determine the appropriate ranges.

### Convex hull
Convex hull and convexity defects play a major role in hand gesture recognition.
```python
hull = cv2.convexHull(contour)  # like contours
```

### Solidity
solidity = contour area / convex hull area
Cannot be larger than 1.
When used to distinguish shapes, one needs to manually inspect the values of solidity to determine the appropriate ranges.
```python
hull_area = cv2.contourArea(hull)
area = cv2.contourArea(contour)
solidity = area / hull_area
```

## 1.11.4 Contour approximation
For reducing the number of points in a curve with a reduced set of points.
The algorithm is commonly known as the Ramer-Douglas-Peucker algorithm, or the split-and-merge algorithm.
Use short line segments to approximate the curve.
```python
perimeter = cv2.arcLength(contour, closed=True)
approx = cv2.approxPolyDP(contour, epsilon=0.01*perimeter, closed=True)
```
We often set `epsilon` to be 1-5% of the perimeter. The larger this value is, the more points will be discarded.

We can examine the number of points within an approximated contour. If there are 4, then it is a rectangular, not a circle.

## 1.11.5 Sorting contours
Sorting contours by positions is solved by sorting their bounding box coordinates.
We can also keeping the largest ones by sorting them first according to their contour areas.

# 1.12 Histograms
Grayscale histograms for thresholding.
Color histograms for object tracking (CamShift algorithm).
Color histograms as features.
Gradient histograms for HOG and SIFT descriptors.

## Grayscale histogram
```python
hist = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
# normalized
hist /= hist.sum()
```
`histSize` is the number of bins.

## Color histogram
Split the image into channels first, and then create histograms for each channel.

## Multi-dimensional histogram
```python
hist = cv2.calcHist([channels[1], channels[0]], channels=[0, 1], mask=None, histSize=[32, 32], ranges=[0, 256, 0, 256])
```

## Histogram equalization
Improves the contrast of an image by "stretching" the distribution of pixels.
Applied to grayscale images.
Useful when an image contains foregrounds and backgrounds that are both dark or both light.
Useful when enhancing the contrast of medical or satellite images.
```python
eq = cv2.equalizeHist(gray)
```

# 1.13 Connected-component labeling
Used to determine the connectivity of "blob"-like regions in a binary image.
Often used in the same situations with contours; but often give us a more granular filtering of the blobs in a binary image.
Can still apply contour properties to extracted components.

## The classical approach
Consists of two passes.

### The first pass
Use union-find data structure.
Loops every pixel and checks the west (W) and north (N) pixels.
1. If the center pixel is a background pixel, ignore it.
2. If both N and W are background, create a new label and assign it to N and W.
3. Label the center pixel to be the minimum of N and W.

### The second pass
Use the union-find data structure to find connected components.

Use `scikit-image`.
```python
labels: np.ndarray = skimage.measure.label(threshed_img, neighbors=8, background=0)
```
The label for background is `0`.
Each position of the return variable has a label number corresponding to that pixel.