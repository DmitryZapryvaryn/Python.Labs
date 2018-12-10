import os
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
from skimage import filters
from skimage import img_as_float
import scipy

# read from URL
logo = io.imread('http://scikit-image.org/_static/img/logo.png')
io.imsave('Lab2/local_logo.png', logo)

# read from directory by path
filename = os.path.join(skimage.data_dir, 'camera.png')
camera = io.imread(filename)
camera_float = img_as_float(camera)
print("Camera max: ", camera.max())
print("Camer float max: ", camera_float.max())

camera_sobel = filters.sobel(camera)
print("Camera sobel max: ", camera_sobel.max())

face = scipy.misc.face()
print("Raccoon image shape: ", face.shape)
plt.figure(3)
plt.imshow(face)

plt.figure(1)
plt.imshow(camera)

plt.figure(2)
plt.imshow(camera_sobel)
plt.show()
