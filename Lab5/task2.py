import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression(normalize=True)
print(model.normalize)
print(model)

x = np.array([0, 1, 2])
y = np.array([0, 1, 2])

X = x[:, np.newaxis]
print('\nX:\n', X)
model.fit(X, y)
print('\nmodel.coef_:\n', model.coef_)
