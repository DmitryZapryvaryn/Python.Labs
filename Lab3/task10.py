import numpy as np
import matplotlib.pyplot as plt

n = 8
X, Y = np.mgrid[-n:n+1, -n:n+1]
cmap = plt.get_cmap("jet")
colors = cmap(np.linspace(0, 0.8, 8))
M = np.hypot(X, Y)
plt.quiver(X, Y, X, Y, M)

plt.axis('off')
'''
X = np.arange(n)
Y = np.arange(n)
U, V = np.meshgrid(X, Y)
plt.quiver(X, Y, U, V)
'''

plt.show()
