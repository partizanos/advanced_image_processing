import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np

# def jpeg(img):

img = mpimg.imread("./test.png")

M, N, O = img.shape
R = np.ndarray(img.shape)
R_DIMENSION = img[:, :, 0]
R[:, :, 0] = R_DIMENSION
R[:, :, 1] = np.zeros((M, N))
R[:, :, 2] = np.zeros((M, N))

G = np.ndarray(img.shape)
G[:, :, 0] = np.zeros((M, N))
G_DIMENSION = img[:, :, 1]
G[:, :, 1] = G_DIMENSION
G[:, :, 2] = np.zeros((M, N))

B = np.ndarray(img.shape)
B[:, :, 0] = np.zeros((M, N))
B[:, :, 1] = np.zeros((M, N))
B_DIMENSION = img[:, :, 2]
B[:, :, 2] = B_DIMENSION

fig, ax = plt.subplots(
    ncols=3,
    sharex=True,
    sharey=True,
    figsize=(30, 30)
)
ax[0].imshow(R)
ax[1].imshow(G)
ax[2].imshow(B)
# %%
Y = np.add(np.add(0.299 * R_DIMENSION, 0.587 * G_DIMENSION), 0.114 * B_DIMENSION)
Cb = - 0.1687 * R_DIMENSION - 0.3313 * G_DIMENSION + 0.5 * B_DIMENSION + 128
Cr = 0.5 * R_DIMENSION - 0.4187 * G_DIMENSION - 0.0813 * B_DIMENSION + 128
R_DIMENSION = Y + 1.402 * (Cr - 128)
G_DIMENSION = Y - 0.34414 * (Cb - 128) - 0.71414 * (Cr - 128)
B_DIMENSION = Y + 1.772 * (Cb - 128)

fig, ax = plt.subplots(
    ncols=3,
    sharex=True,
    sharey=True,
    figsize=(30, 30)
)
ax[0].imshow(Y, cmap="gray")
ax[1].imshow(Cb)
ax[2].imshow(Cr)

#######################
from PIL import Image
image = Image.open("./test.png")
ycbcr = image.convert('YCbCr')
plt.imshow(ycbcr)
npmat = np.array(ycbcr, dtype=np.uint8)
ready_Y = npmat[:,:,0]
ready_Cb = npmat[:,:,1]
ready_Cr = npmat[:,:,2]

fig, ax =  plt.subplots(
        ncols=3,
        sharex=True,
        sharey=True,
        figsize=(30, 30)
)
ax[0].imshow(ready_Y, cmap="gray")
ax[1].imshow(ready_Cb)
ax[2].imshow(ready_Cr)

################

def downsample_image(img, skip):
    return img[::skip,::skip]

d_cb  = downsample_image(ready_Cb, 2)
d_cb  = downsample_image(d_cb, 2)

d_cr  = downsample_image(ready_Cr, 2)
d_cr  = downsample_image(d_cr, 2)

fig, ax =  plt.subplots(
        ncols=2,
        sharex=True,
        sharey=True,
        figsize=(30, 30)
)
ax[0].imshow(ready_Cr)
ax[1].imshow(d_cr, cmap="gray")
##############################################



from sklearn.feature_extraction import image


patches = image.extract_patches_2d(img, (8, 8), random_state=0)





