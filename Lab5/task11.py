import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA

iris = load_iris()
X = iris.data
y = iris.target

pca = PCA(n_components=2, whiten=True)
pca.fit(X)
print('pca.components_:\n', pca.components_)
print('pca.explained_variance_ratio_:\n', pca.explained_variance_ratio_)
X_pca = pca.transform(X)
print('X_pca.shape: ', X_pca.shape)

target_ids = range(len(iris.target_names))
for i, c, label in zip(target_ids, 'rgbcmykw', iris.target_names):
    plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1],
                c=c, label=label)

plt.show()
