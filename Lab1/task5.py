import numpy as np

a = np.floor(10*np.random.random((3, 4)))
print('a:\n', a)
print('a.shape: ', a.shape)
print('a.ravel(): ', a.ravel())
print('a.reshape():\n', a.reshape(6, 2))
print('a.T:\n', a.T)
print('a.T.shape: ', a.T.shape)
print('a.shape: ', a.shape)
a = np.floor(10*np.random.random((3, 4)))
print('a:\n', a)
a.resize((2, 6))
print('after a.resize(2, 6):\n', a)
a.reshape(3, -1)
print('after a.reshape(3, -1):\n', a)
b = a.reshape(3, -1)
print('after b = a.reshape(3, -1):\n', b)