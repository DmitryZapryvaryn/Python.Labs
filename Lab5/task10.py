import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_diabetes, load_digits
from sklearn.linear_model import Ridge, Lasso
from sklearn.grid_search import GridSearchCV
from sklearn.linear_model import RidgeCV, LassoCV

digits = load_digits()
X = digits.data
y = digits.target

clf = KNeighborsClassifier()
cross_val_score(clf, X, y, cv=5)

cv = ShuffleSplit(n_splits=5)
cross_val_score(clf, X, y, cv=cv)

data = load_diabetes()
X, y = data.data, data.target
print(X.shape)

for Model in [Ridge, Lasso]:
    model = Model()
    print('%s: %s' % (Model.__name__, cross_val_score(model, X, y).mean()))

alphas = np.logspace(-3, -1, 30)

for Model in [Lasso, Ridge]:
    scores = [cross_val_score(Model(alpha), X, y, cv=3).mean()
              for alpha in alphas]
    plt.plot(alphas, scores, label=Model.__name__)

for Model in [Ridge, Lasso]:
    gscv = GridSearchCV(Model(), dict(alpha=alphas), cv=3).fit(X, y)
    print('%s: %s' % (Model.__name__, gscv.best_params_))

for Model in [RidgeCV, LassoCV]:
    model = Model(alphas=alphas, cv=3).fit(X, y)
    print('%s: %s' % (Model.__name__, model.alpha_))

plt.show()
