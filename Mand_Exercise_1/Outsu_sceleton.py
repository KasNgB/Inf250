# -*- coding: utf-8 -*-

"""
Skeleton for first part of the blob-detection coursework as part of INF250
at NMBU (Autumn 2017).
"""

__author__ = "Kasper Ng Bergan"
__email__ = "kasper.ng.bergan@nmbu.no"

import numpy as np
import cv2


img_path = 'gingerbread.jpg'
gingerbread = cv2.imread(img_path)

def threshold(image, th=None):
    """Returns a binarised version of given image, thresholded at given value.

    Binarises the image using a global threshold `th`. Uses Otsu's method
    to find optimal thrshold value if the threshold variable is None. The
    returned image will be in the form of an 8-bit unsigned integer array
    with 255 as white and 0 as black.

    Parameters:
    -----------
    image : np.ndarray
        Image to binarise. If this image is a colour image then the last
        dimension will be the colour value (as RGB values).
    th : numeric
        Threshold value. Uses Otsu's method if this variable is None.

    Returns:
    --------
    binarised : np.ndarray(dtype=np.uint8)
        Image where all pixel values are either 0 or 255.
    """
    # Setup
    shape = np.shape(image)
    binarised = np.zeros([shape[0], shape[1]], dtype=np.uint8)
    if len(shape) == 3:
        image = image.mean(axis=2)
    elif len(shape) > 3:
        raise ValueError('Must be at 2D image')

    if th is None:
        th = otsu(image)

    # Start thresholding
    ## WRITE YOUR CODE HERE
    binarised[image > th] = 255

    return binarised


def histogram(image):
    """Returns the image histogram with 256 bins.
    """
    # Setup
    shape = np.shape(image)
    histogram = np.zeros(256)

    if len(shape) == 3:
        image = image.mean(axis=2)
    elif len(shape) > 3:
        raise ValueError('Must be at 2D image')

    # Start to make the histogram
    ## WRITE YOUR CODE HERE

    for height_index in range(shape[0]):
        for width_index in range(shape[1]):
            histogram_index = int(image[height_index][width_index])
            histogram[histogram_index] += 1

    return histogram


def otsu(image):
    """Finds the optimal thresholdvalue of given image using Otsu's method.
    """
    hist = histogram(image)
    final_bcv = 0
    th_final = 0

    ## WRITE YOUR CODE HERE
    total = sum(hist)
    for th in range(len(hist)):

        hist_sum0 = sum(hist[:th])
        hist_sum1 = sum(hist[th:])

        if hist_sum0 == 0 or hist_sum1 == 0:
            continue

        omega0 = hist_sum0/total
        mean0 = sum(i * hist[i] for i in range(th)) / hist_sum0

        omega1 = hist_sum1/total
        mean1 = sum(i * hist[i] for i in range(th, len(hist))) / hist_sum1

        bcv = np.sqrt(omega0*omega1 * (mean1 - mean0)**2) 

        if bcv > final_bcv:
            final_bcv = bcv
            th_final = th

    return th_final


