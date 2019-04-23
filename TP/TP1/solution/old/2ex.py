import random
import matplotlib.pyplot as plt
import cv2
import math
from helpers import mse
from PIL import Image
import copy
import scipy.misc
import numpy as np


print("2_ex.py")


def psnr(img1, img2, alpha=8):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


# Exercise 2. ex
# (a) Refractor the PNSR definition such that the PSNR is expressed as
# a function of the noise variance σ^2


def mse_from_psnr(psnr, alpha):
    mse_v = math.pow(10, ((psnr - 20 * math.log10(alpha)) / -10))
    return mse_v


# (b) Add Gaussian noise to an image such that the PSNR ratio with the original image is
# 10dB, 20dB, 30dB and 40dB. Use randn, not imnoise.


def get_img_with_gaussian_noise(im, sigma, mu=0):
    for i in range(0, len(im)-1):
        for j in range(0, len(im[i])-1):
            noise = sigma * np.random.randn() + mu
            im[i][j] = noise + float(im[i][j])
    return im


alpha = 8
sigmas = [ mse_from_psnr(psnr_var, alpha) for psnr_var in [10, 20, 30, 40]]
images = [(get_img_with_gaussian_noise(scipy.misc.imread('data/cameraman.tif'), s), s) for s in sigmas]
# images = [(get_img_with_noise(scipy.misc.imread('data/cameraman.tif'), s), s) for s in [0.1, 0.01, 0.001, 0.0001]]

    # cameraman_image_changed = cameraman_image_or

# (c) Show the noisy images on the screen. How do they look?
def save(i, s):
    im = Image.fromarray(i)
    im.save("ex2_" + str(s) + ".png")

[save(i,s) for (i, s) in images]
# (d) Show the histograms for these noisy images, can you explain what you see?

def histo(img, name):
    plt.hist(img.ravel(),256,[0,256]);
    plt.savefig(name + ".png")
    # plt.show()

[ histo(i, str(s)+"histo") for (i, s) in images]
