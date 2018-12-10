import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage import filters
from skimage import measure

camera = data.camera()
val = filters.threshold_otsu(camera)
mask = camera < val
all_labels = measure.label(mask, background=10)

plt.figure()
plt.subplot(121), plt.axis('off')
plt.imshow(camera, cmap='gray')
plt.subplot(122), plt.axis('off')
plt.imshow(camera, cmap='gray')
plt.imshow(all_labels, cmap='hot', alpha=0.7)

n = 20
l = 256
im = np.zeros((l, l))
points = l * np.random.random((2, n**2))
im[(points[0]).astype(np.int), (points[1]).astype(np.int)] = 1
im = filters.gaussian(im, sigma=l / (4. * n))
blobs = im > im.mean()
all_labels = measure.label(blobs)
blobs_label = measure.label(blobs, background=0)

plt.figure()
plt.subplot(121), plt.axis('off')
plt.imshow(im, cmap='gray')
plt.subplot(122), plt.axis('off')
plt.imshow(blobs_label, cmap='gray')
plt.show()
