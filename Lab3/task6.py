import numpy as np
import matplotlib.pyplot as plt

n = 12
X = np.arange(n)
Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

for x, y1, y2 in zip(X, Y1, Y2):
    plt.text(x, y1 + 0.05, '%.2f' % y1, ha='center', va='bottom')
    plt.text(x, -y2 - 0.15, '%.2f' % y2, ha='center', va='bottom')

plt.ylim(-1.25, +1.25)

plt.show()
