import numpy as np

a = np.arange(12)**2
print('a:\n', a)
i = np.array([1, 1, 3, 8, 5])  # массив индексов
print('a[i]: ', a[i])
j = np.array([[3, 4], [9, 7]])  # матрица индексов
print('a[j]: ', a[j])
a = np.arange(12).reshape(3, 4)
print('a:\n', a)
b = a > 4
print('b = a > 4:\n', b)
print('a[b]:\n', a[b])
