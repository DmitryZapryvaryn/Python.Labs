import numpy as np
import matplotlib.pyplot as plt

# np.random.uniform(0, 1, 20)

Z = np.ones(20)
Z[-1] = 2
explode = np.zeros(20)
explode[:] = 0.05
explode[-1] = 0.5
cmap = plt.get_cmap("gray")
colors = cmap(np.linspace(0, 0.8, 20))
plt.pie(
    Z, startangle=0, explode=explode,
    wedgeprops=dict(linewidth=.5, edgecolor='black'),
    colors=colors)

plt.show()
