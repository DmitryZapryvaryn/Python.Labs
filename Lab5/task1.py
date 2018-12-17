from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

iris = load_iris()

print('iris.data.shape: ', iris.data.shape)
n_samples, n_features = iris.data.shape
print('n_samples: ', n_samples)
print('n_features: ', n_features)
print('iris.data[0]:\n', iris.data[0])

print('iris.target.shape: ', iris.target.shape)
print('iris.target:\n', iris.target)
print('iris.target_names:\n', iris.target_names)

X = iris.data[:, :2]
y = iris.target

fig, ax = plt.subplots()
cax = ax.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', edgecolor='k')
plt.xlabel('Sepal length(cm)')
plt.ylabel('Sepal width(cm)')
cbar = fig.colorbar(cax, ticks=[0, 1, 2])
cbar.ax.set_yticklabels(iris.target_names)

plt.show()
