import numpy as np
import matplotlib.pyplot as plt

check = np.zeros((9, 9))
# :: => start : end : step ((0, end of array, 1) - default values)
check[::2, 1::2] = 1
check[1::2, ::2] = 1
plt.imshow(check, cmap='gray', interpolation='nearest')
plt.show()
