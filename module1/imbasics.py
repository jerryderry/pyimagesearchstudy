import numpy as np
import cv2


def translate(image: np.ndarray, x: float, y: float) -> np.ndarray:
    """Translate an image with x pixels horizontally
    and y pixels vertically.
    """
    # Construct the translation matrix
    M = np.array([[1, 0, x], [0, 1, y]], np.float32)
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted


def rotate(image: np.ndarray, angle: float, *, around:tuple = None, scale=1.0):
    """Rotate an image around a given center."""
    # Image dimensions
    (height, width) = image.shape[0:2]
    # Rotation center
    if around is None:
        center = (width//2, height//2)
    else:
        center = around

    # Construct rotation matrix
    R = cv2.getRotationMatrix2D(center, angle, scale)

    rotated = cv2.warpAffine(image, R, (width, height))
    return rotated


def resize(image: np.ndarray, *, width: int = None, height: int = None, interpolation=cv2.INTER_AREA):
    """Resize an image to the given dimensions.
    If width or height is None, then the image keeps its original aspect ratio.
    If width and height are both None, then simply return the original image.
    If both width and height are given, the original aspect ratio will be ignored.
    """
    if width is None and height is None:
        return image

    aspect_ratio = image.shape[1] / image.shape[0]

    if width is None and height is not None:
        resized_width = int(aspect_ratio * height)
        return cv2.resize(image, (resized_width, height), interpolation)
    if width is not None and height is None:
        resized_height = int(width / aspect_ratio)
        return cv2.resize(image, (width, resized_height), interpolation)

    return cv2.resize(image, (width, height), interpolation)

def auto_canny(img: np.ndarray, sigma: float = 0.33):
    """Apply the Canny edge detector to a single channel image by automatically
    calculating the upper and lower thresholds based upon the median pixel
    intensities and a standard deviation.
    """
    assert img.ndim == 2
    median = np.median(img)

    # calculate upper and lower threshold values by adding
    # and substracting one standard deviation
    upper = int(min(255, (1.0 + sigma) * median))
    lower = int(max(0, (1.0 - sigma) * median))

    return cv2.Canny(img, lower, upper)
