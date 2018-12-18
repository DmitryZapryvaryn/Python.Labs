import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


def f(t):
    return 1.2 * t**2 + .1 * t**3 - .4 * t**5 - .5 * t**9

rng = np.random.RandomState(0)
x = 2 * rng.rand(100) - .5
y = f(x) + .4 * rng.normal(size=100)

plt.figure(figsize=(6, 4))
plt.scatter(x, y, s=4)

x_test = np.linspace(-1, 1, 100)
X = np.array([x**i for i in range(5)]).T
X_test = np.array([x_test**i for i in range(5)]).T
regr = linear_model.LinearRegression()
regr.fit(X, y)
plt.plot(x_test, regr.predict(X_test), label='4th order')

X = np.array([x**i for i in range(10)]).T
X_test = np.array([x_test**i for i in range(10)]).T
regr = linear_model.LinearRegression()
regr.fit(X, y)
plt.plot(x_test, regr.predict(X_test), label='9th order')

plt.ylim(-2, 4)
plt.legend()

plt.show()
