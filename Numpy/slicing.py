import numpy as np

a = np.array([1, 2, 3])
# accessing particular index
print(f"Element at third position is {a[2]}")
# accessing more than one element in sequence = slicing
print(f"Element from 1 to 3 position {a[0:3]}")

b = np.array([[1, 2], [3, 4], [5, 6]])
# element at second row first column is
print(f"Second row and third column element is {b[1, 0]}")
print(f"First value from each row {b[:, 0]}")
print(f"second value from first two rows {b[:2, 1]}")
c = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
print(f"Last two values from each row {c[:,-2:]}")
