import numpy as np
import matplotlib.pyplot as plt

axes = plt.gca()
axes.set_xlim(0, 4)
axes.set_ylim(0, 3)

major_ticks = np.arange(0, 101, 20)
minor_ticks = np.arange(0, 101, 5)

axes.set_xticklabels([])
axes.set_yticklabels([])

axes.set_xticks(major_ticks)
axes.set_xticks(minor_ticks, minor=True)
axes.set_yticks(major_ticks)
axes.set_yticks(minor_ticks, minor=True)

# And a corresponding grid
axes.grid(which='both')

# Or if you want different settings for the grids:
axes.grid(which='minor', alpha=0.2)
axes.grid(which='major', alpha=0.5)

plt.show()
