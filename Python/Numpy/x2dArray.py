import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
print(f"This is a {a.ndim} dimensional array")
print(a[1][1])
print(f"Size of array is {a.size}")
print(f"Shape of array is {a.shape}")
print(f"Type of array is {a.dtype}")
print(f"Size of each element is {a.itemsize}")
