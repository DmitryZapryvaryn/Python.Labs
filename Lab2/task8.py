import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage import filters
from skimage import measure
from skimage import morphology
from skimage.feature import canny
from skimage.feature import peak_local_max
from skimage.segmentation import random_walker
from scipy import ndimage

coins = data.coins()

# Оцу
val = filters.threshold_otsu(coins)
mask = coins < val
labels_otsu = measure.label(mask, background=6)

# метод адаптивной пороговой сегментации
# filters.threshold_adaptive() (deprecated)
threshold_image = filters.threshold_local(
    coins, block_size=15)

# watershed
edges = canny(coins)
fill_coins = ndimage.binary_fill_holes(edges)
markers = np.zeros_like(coins)
markers[coins < 35] = 1
markers[coins > 155] = 2

labels_ws = morphology.watershed(fill_coins, markers, mask=coins)

# random walker
# markers[~coins] = 2
labels_rw = random_walker(coins, markers, beta=10000)

fig, axes = plt.subplots(
    1, 5, figsize=(10, 10), sharex=True, sharey=True)

ax = axes.ravel()
ax[0].set_title('Original')
ax[0].imshow(coins)

ax[1].set_title('Otsu')
ax[1].imshow(coins)
ax[1].imshow(labels_otsu, alpha=0.7)

ax[2].set_title('Threshold local')
ax[2].imshow(threshold_image)

ax[3].set_title('Watershed')
ax[3].imshow(labels_ws)

ax[4].set_title('Random walker')
ax[4].imshow(labels_rw)

for a in ax.ravel():
    a.axis('off')
fig.tight_layout()

plt.show()
