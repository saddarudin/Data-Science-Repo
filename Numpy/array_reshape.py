import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 7, 2]])
x, y = a.shape
print(f"Shape of array is {x, y}")
a = a.reshape(y, x)
print(f"Shape of array is {a.shape}")
# It can also be reshaped according to order you want it to be.
# But the total size must be same mean m*n must be same for both arrays
a = a.reshape(2, 6)
print(f"Shape of array is {a.shape}")
print(a)
