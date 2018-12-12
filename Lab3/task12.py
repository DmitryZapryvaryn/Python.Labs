import matplotlib.pyplot as plt

ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 3, 4)
ax3 = plt.subplot(2, 3, 5)
ax4 = plt.subplot(2, 3, 6)

for ax in [ax1, ax2, ax3, ax4]:
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_yticks([])
    ax.set_xticks([])

plt.show()
