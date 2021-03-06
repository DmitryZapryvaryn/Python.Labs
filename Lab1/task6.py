import numpy as np
from numpy import newaxis

a = np.floor(10*np.random.random((2, 2)))
b = np.floor(10*np.random.random((2, 2)))
print('a:\n', a)
print('b:\n', b)
v = np.vstack((a, b))
h = np.hstack((a, b))
print('v:\n', v)
print('h:\n', h)

d = np.column_stack((a, b))
print('d:\n', d)
print('-----------------------------------------------------------')
a = np.array([4., 2.])
b = np.array([3., 8.])
print('a:\n', a)
print('b:\n', b)
d = np.column_stack((a, b))
print('d column_stack:\n', d)
d = np.hstack((a, b))
print('d hstack:\n', d)
print('a[:, newaxis]:\n', a[:, newaxis])
print('np.column_stack((a[:, newaxis], b[:, newaxis]))')
print(np.column_stack((a[:, newaxis], b[:, newaxis])))
print('np.hstack((a[:, newaxis], b[:, newaxis]))')
print(np.hstack((a[:, newaxis], b[:, newaxis])))

print('-----------------------------------------------------------')
a = np.floor(10*np.random.random((2, 12)))
print('a:\n', a)
d1 = np.hsplit(a, 3)
print('d1:\n', d1)
d2 = np.hsplit(a, (3, 4))
print('d2:\n', d2)

print('-----------------------------------------------------------')

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print('a:\n', a)
print('b:\n', b)

conc = np.concatenate((a, b), axis=0)
print('conc by columns:\n', conc)

conc = np.concatenate((a, b), axis=1)
print('conc by rows:\n', conc)

print('-----------------------------------------------------------')

print('a:\n', a)
print('b:\n', b)
print('c_[a, b]:\n', np.c_[a, b])
print('r_[a, b]:\n', np.r_[a, b])
