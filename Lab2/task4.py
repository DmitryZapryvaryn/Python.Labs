import numpy as np
from matplotlib import pyplot as plt
from skimage import data
from skimage import filters
from skimage import exposure
from skimage import morphology
from skimage import restoration
from skimage.morphology import disk


def orig_vs_changed(orig_image, changed_image, changed_title):
    fig, axes = plt.subplots(1, 2)
    ax = axes.ravel()
    ax[0].imshow(orig_image, cmap='gray')
    ax[0].set_title("Original image")
    ax[1].imshow(changed_image, cmap='gray')
    ax[1].set_title(changed_title)
    for a in ax.ravel():
        a.axis('off')
    fig.tight_layout()

# ------ DATA ---------- #
text = data.text()
camera = data.camera()
coins = data.coins()

# ------ sobel ----------- #
hsobel_text = filters.sobel_h(text)

# ------ equalize_hist --- #
camera_equalized = exposure.equalize_hist(camera)

# ------ dilation -------- #
a = np.zeros((5, 5), dtype=np.uint8)
a[2, 2] = 1
print('a:\n', a)
b = morphology.binary_dilation(a, morphology.diamond(1)).astype(np.uint8)
print('b:\n', b)

# ------ resoration ------ #
coins_zoom = coins[10:80, 300:370]
median_coins = filters.median(coins_zoom, disk(1))
tv_coins = restoration.denoise_tv_chambolle(coins_zoom, weight=0.1)
gaussian_coins = filters.gaussian(coins_zoom, sigma=2)

# ------ show ------------ #
orig_vs_changed(text, hsobel_text, 'Sobel')
orig_vs_changed(camera, camera_equalized, 'Equalized')
orig_vs_changed(a, b, 'Dilation')

fig, axes = plt.subplots(2, 2)
ax = axes.ravel()

ax[0].imshow(coins_zoom)
ax[0].set_title("Original image")

ax[1].imshow(median_coins)
ax[1].set_title('Median')

ax[2].imshow(tv_coins)
ax[2].set_title('Denoise')

ax[3].imshow(gaussian_coins)
ax[3].set_title('Gaussian')

for a in ax.ravel():
    a.axis('off')
fig.tight_layout()

plt.show()
