from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt

digits = load_digits()

pca = PCA(n_components=2)
proj = pca.fit_transform(digits.data)

X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target)

clf = GaussianNB()
clf.fit(X_train, y_train)

predicted = clf.predict(X_test)
expected = y_test
print('\npredicted:\n', predicted)
print('\nexpected:\n', expected)

matches = (predicted == expected)
print('Matches sum: ', matches.sum())
print('Matches len: ', len(matches))
k = matches.sum() / float(len(matches))
print(k)

print('\nReport:\n', metrics.classification_report(expected, predicted))
print('\Confusion matrix:\n', metrics.confusion_matrix(expected, predicted))

plt.show()
