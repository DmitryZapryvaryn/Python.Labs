import matplotlib.pyplot as plt
import numpy as np

import skimage
from skimage import data


# help(skimage)

img = data.camera()
print("Camera's image shape: ", img.shape)
print("Camera's image size: ", img.size)

my_image = data.coffee()
plt.imshow(my_image)
plt.show()
