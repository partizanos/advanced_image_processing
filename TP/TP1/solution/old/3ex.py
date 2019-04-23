import matplotlib.pyplot as plt
import cv2
import math
from helpers import mse
from PIL import Image
import copy
import scipy.misc
import numpy as np

print("ex3.py")

# Exercise 3. Read the image peppers.png and convert it to grayscale. Perform its low-rank
# approximation for k = 1, ..., n. Plot the dependence between the k and MSE of k-rank approximation
# version of original image. Make a conclusion

im = scipy.misc.imread('data/peppers.png')
