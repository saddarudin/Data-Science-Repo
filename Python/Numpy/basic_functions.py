import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# Minimum
print(f"Minimum value in array is {a.min()}")
# Maximum
print(f"Maximum value in the array is {a.max()}")
# Sum
print(f"Sum of all the elements of the array is {a.sum()}")
# axis = 0 for columns and axis = 1 for rows
print(f"Sum of elements in rows is {a.sum(axis=1)}")
print(f"Sum of elements in columns is {a.sum(axis=0)}")
