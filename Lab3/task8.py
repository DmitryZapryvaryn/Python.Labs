import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable


def f(x, y):
    return (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

n = 10
x = np.linspace(-3, 3, 4 * n)
y = np.linspace(-3, 3, 3 * n)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig, ax = plt.subplots()
im = plt.imshow(Z)
ax.invert_yaxis()

divider = make_axes_locatable(ax)
ax_cb = divider.append_axes('right', size="5%", pad=0.2)

fig.colorbar(im, cax=ax_cb)

plt.show()
