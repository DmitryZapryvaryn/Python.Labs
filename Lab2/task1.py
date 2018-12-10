import matplotlib.pyplot as plt
import numpy as np

import skimage
from skimage import data


# help(skimage)

img = data.camera()
print("Camera's image shape: ", img.shape)
print("Camera's image size: ", img.size)

my_image = data.coffee()

# red channel
r = my_image[:, :, 0]
r_min = np.min(r)
r_max = np.max(r)
print("Min, max of red channel: ", r_min, ", ", r_max)

# green channel
g = my_image[:, :, 1]
g_min = np.min(g)
g_max = np.max(g)
print("Min, max of green channel: ", g_min, ", ", g_max)

# blue channel
b = my_image[:, :, 2]
b_min = np.min(b)
b_max = np.max(b)
print("Min, max of blue channel: ", b_min, ", ", b_max)

# Mask
print("Median of blue channel: ", np.median(b))
mask = my_image[:, :, 2] < np.median(b)
my_image[mask] = [0, 0, 0]
plt.imshow(my_image)
plt.show()

'''
fig, axes = plt.subplots(2, 2, figsize=(7, 6), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(my_image)
ax[0].set_title("Original image")

ax[1].imshow(r)
ax[1].set_title("Red")

ax[2].imshow(g)
ax[2].set_title("Green")

ax[3].imshow(b)
ax[3].set_title("Blue")

for a in ax.ravel():
    a.axis('off')

fig.tight_layout()
plt.show()
'''
