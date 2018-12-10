import numpy as np

a = np.arange(999979, 999999, dtype=np.int16).reshape(10, 2)

print("Matrix \'a\':\n ", a)
print("Matrix dimension: ", a.ndim)
print("Matrix data type: ", a.dtype)
print("Matrix item size: ", a.itemsize, " bytes")
print("Matrix shape: ", a.shape)
print("Matrix size: ", a.size)

b = np.array([6, 7, 8])
print("\nArray \'b\':", b)
