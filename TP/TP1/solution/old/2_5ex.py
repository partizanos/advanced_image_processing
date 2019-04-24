
import random
import matplotlib.pyplot as plt
import cv2
import math
from helpers import mse
from PIL import Image
import copy
import scipy.misc
import numpy as np


# (e) Add salt & pepper Noise to an image until the PSNR ratio between the original and the
# noisy image is 40 dB. Visually compare it to the 40dB noisy image to which Gaussian
# noise was added. What can you conclude?


def psnr(img1, img2, alpha=8):
    mse = np.mean( (img1 - img2) ** 2 )
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))

def get_img_with_pepper_salt_noise(img, p=0.4, q=0.7):
        im = copy.deepcopy(img)
    for i in range(0, len(im)-1):
        for j in range(0, len(im[i])-1):
            r = random.random()
            val=im[i][j]
            if(r < p):
                val = 0.0
            elif(r < q):
                val = 255
            im[i][j] = val
    return im

img = scipy.misc.imread('data/cameraman.tif')

noised = get_img_with_pepper_salt_noise(img)
psnrV=0
while(psnrV  < 40):
    print("adding salt pepper noise")
    noised = get_img_with_pepper_salt_noise(noised)
    # print("noised")
    # print(noised)
    # print("img")
    # print(img)
    psnrV = psnr(img, noised)
    print(psnrV)
plt.savefig("pepperNoise.png")
print("END")
