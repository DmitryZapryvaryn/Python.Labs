import numpy as np
from matplotlib import pyplot as plt
from skimage import morphology
from skimage import segmentation
from skimage.feature import peak_local_max
from scipy import ndimage

x, y = np.indices((80, 80))
x1, y1, x2, y2 = 28, 28, 44, 52
r1, r2 = 16, 20
mask_circle1 = (x - x1) ** 2 + (y - y1) ** 2 < r1 ** 2
mask_circle2 = (x - x2) ** 2 + (y - y2) ** 2 < r2 ** 2
image = np.logical_or(mask_circle1, mask_circle2)

distance = ndimage.distance_transform_edt(image)
local_maxi = peak_local_max(
    distance, indices=False, footprint=np.ones((3, 3)), labels=image)
markers = morphology.label(local_maxi)
markers[~image] = -1
labels_rw = segmentation.random_walker(image, markers)

plt.figure()
plt.subplot(131), plt.axis('off')
plt.imshow(image, cmap='gray')
plt.subplot(132), plt.axis('off')
plt.imshow(markers, cmap='gray')
plt.subplot(133), plt.axis('off')
plt.imshow(labels_rw, cmap='Paired')

plt.show()
