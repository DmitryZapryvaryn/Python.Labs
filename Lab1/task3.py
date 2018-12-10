import numpy as np

a = np.array([20, 30, 40, 50])
print("\'a\': ", a)
b = np.arange(4)
print("\'b\': ", b)
c = a-b
print("\'c\': ", c)
d = b**2
print("\'d\': ", d)
f = 10*np.sin(a)
print("\'f\': ", f)
k = a < 35
print("\'k\': ", k)

##################################################
print()

A = np.array([[1, 1], [0, 1]])
print("A:\n", A)
B = np.array([[2, 0], [3, 4]])
print("B:\n", B)

D = A * B
print("D:\n", D)
P = np.dot(A, B)
print("P:\n", P)

##################################################
print()

b = np.arange(12).reshape(3, 4)
print(b)
np.sum
s1 = b.sum(axis=0)
print("columns: ", s1)
s2 = b.sum(axis=1)
print("rows: ", s2)
matrix_sum = b.sum()
print("sum of matrix elements: ", matrix_sum)
