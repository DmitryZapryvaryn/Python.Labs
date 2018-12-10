import numpy as np
import os

print("\n----\'a\'----\n")
a = np.array([2, 3, 4])
print(a)
print(a.dtype)

###############################################################################
print("\n----\'b\'----\n")
b = np.array([1.2, 3.5, 5.1])
print(b)
print(b.dtype)

b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print(b.dtype)

###############################################################################
print("\n----\'c\'----\n")
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)

###############################################################################
print("\n----\'d\'----\n")
d = np.arange(0, 2, 0.5)
print("arange: ", d)
d = np.linspace(0, 2, 9)
print("linespace: ", d)

###############################################################################
print("\n----\'e, x, f\'----\n")
e = np.linspace(0, 2, 9)
x = np.linspace(0, 2*np.pi, 100)
f = np.sin(x)
print(e, x, f)

###############################################################################
print("\n----zeros----\n")
zeros_matrix = np.zeros((3, 4))
print(zeros_matrix)

print("zeros_like of \'a\': ", np.zeros_like(a))

###############################################################################
print("\n----ones----\n")
ones_matrix = np.ones((3, 4))
print(ones_matrix)

print("ones_like of \'a\': ", np.ones_like(a))

###############################################################################
print("\n----empty----\n")

empty_matrix = np.empty((2, 2), dtype=np.int16)
print(empty_matrix)
empty_like_matrix = np.empty_like(d)
print("empty_like of \'d\':\n", empty_like_matrix)

###############################################################################
print("\n----random----\n")

random_array = np.random.rand(2)
print("Simple rand: ", random_array)

norm_rand_matrix = np.random.randn(4, 4)
print("Normal distribution rand:\n", norm_rand_matrix)

###############################################################################
print("\n----fromfunction----\n")


def custom_function(x, y):
    return x*10 + y**2

fromfunction_matrix = np.fromfunction(custom_function, (3, 3))
print(fromfunction_matrix)

###############################################################################
print("\n----fromfile----\n")

fromfile_array = np.fromfile("Lab1/test_data.txt", sep=' ', dtype=np.int32)
print(fromfile_array)
