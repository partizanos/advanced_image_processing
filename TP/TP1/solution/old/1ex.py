import matplotlib.pyplot as plt
from PIL import Image
import scipy.misc
import numpy as np
import cv2
from helpers import mse


def experiment(max, name, norm):
    def im2double(im, max, norm):
        # Convert to normalized floating point
        print(norm)
        print(type(norm))
        print("norm==32")
        out = cv2.normalize(
            im,
            None,
            0,
            max,
            norm
        )
        return out

        ##########
        # Exercise 1. ex
        # (a) Write a function that determines the Mean Squared Error (MSE) between
        # two images x and y
        ##########

    # (b) Read in a new copy of the image cameraman.tif,
    # keep it in its original datatype and
    # range, i.e. uint8 and {0..255}.
    ##########

    global cameraman_image_original
    cameraman_image_original = scipy.misc.imread('data/cameraman.tif')
    # cameraman_image_original = Image.open(cameraman_image_original)

    ##########

    # (c) Now read in a second copy of the image cameraman.tif
    # but map it to double and {0..1}.
    ##########

    # Convert to normalized floating point
    global cameraman_image_changed
    cameraman_image_changed = cameraman_image_original
    ## working
    cameraman_image_changed = im2double(cameraman_image_original,max, norm)

    ##########
    # See Matlab im2double.
    # https://stackoverflow.com/questions/29100722/equivalent-im2double-function-in-opencv-python
    ##########


    ##########
    # Compare the two images using the MSE. Can you explain the result?
    error = mse(cameraman_image_original, cameraman_image_changed)
    print(error)
    #####
    # RESULT
    # 17842.7666309

    # EXPLANATION
    # I compare the version “double”  of the image with the
    # original “uint8” version.
    # the MSE metrics, gave  result  Mean Squared Error of
    # 17842.7666309
    # since the MSE doesn’t consider different
    # information representation.

    # print("cameraman_image_original")
    # print(len(cameraman_image_original))
    # print(cameraman_image_original)
    # print("cameraman_image_changed")
    # print(len(cameraman_image_changed))
    # print(cameraman_image_changed)


    def imgshow(img, name):
        changedImg = Image.fromarray(img)
        # print(changedImg)
        # plt.imshow(changedImg)
        plt.show(changedImg)
        changedImg.save(name +  ".tiff")


    imgshow(cameraman_image_original, "cameraman_image_original" + str(name))
    imgshow(cameraman_image_changed, "cameraman_image_changed" + str(name))
    # print(cameraman_image_original[10:20])
    # print(cameraman_image_changed[10:20])
    print("(max, name, cv2norm):  ", (max, name, norm))
    return (max, name, norm)


# results = []
# for norm in [
#     cv2.NORM_MINMAX,
#     cv2.NORM_INF
# ]:
#     for index in [1, 10, 100, 1000]:
#         for exp in ["0", "1", "2", "3"]:
#             print("DEBUG", (index, exp, norm))
#             results.append(experiment(index, exp, norm))
#
# print((results.sort()))


(experiment(1, "0", cv2.NORM_MINMAX))

print("END")
