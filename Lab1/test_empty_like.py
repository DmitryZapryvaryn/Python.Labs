import numpy as np

empty_matrix = np.empty((2, 2), dtype=np.int32)
print(empty_matrix)
empty_like_matrix = np.empty_like([2., 3., 4., 5.])
print("empty_like of \'d\':\n", empty_like_matrix)
