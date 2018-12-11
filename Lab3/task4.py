import numpy as np
import matplotlib.pyplot as plt

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)
up_Y = Y + 1
bottom_Y = Y - 1

plt.figure(figsize=(8, 5), dpi=80)
plt.axis('off')
plt.plot(X, Y + 1, color='blue', alpha=1.00)
plt.plot(X, Y - 1, color='blue', alpha=1.00)

plt.fill_between(X, up_Y, 1, color='blue', alpha=0.3)
plt.fill_between(
    X, bottom_Y, -1, where=bottom_Y >= -1, color='blue', alpha=0.3)
plt.fill_between(
    X, bottom_Y, -1, where=bottom_Y <= -1, color='red', alpha=0.3)

plt.show()
