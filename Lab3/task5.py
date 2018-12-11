import numpy as np
import matplotlib.pyplot as plt

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
color = np.arctan(Y/X)

plt.scatter(
    X, Y, c=color, cmap=plt.get_cmap('winter'), alpha=0.7, marker='.')

plt.show()
