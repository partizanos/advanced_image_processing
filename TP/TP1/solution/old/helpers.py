import cv2
import numpy as np


def im2double(im):
    # Convert to normalized floating point
    out = cv2.normalize(
        im.astype('float'),
        None,
        0.0,
        1.0,
        cv2.NORM_MINMAX
    )
    return out


def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    return err
