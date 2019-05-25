import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def mse(imageA, imageB) -> float:
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	return err