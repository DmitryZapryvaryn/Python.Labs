from sklearn import neighbors, datasets
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

iris = datasets.load_iris()
X, y = iris.data[:, :2], iris.target
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)

'''
print(
    'Predicted iris name([3, 5, 4, 2]): ', iris.target_names[knn.predict(
        [[3, 5, 4, 2]])])
'''
x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

print(np.c_[xx.ravel(), yy.ravel()].shape)
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

plt.figure()
plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.axis('tight')

plt.show()
