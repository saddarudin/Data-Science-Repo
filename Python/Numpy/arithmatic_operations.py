import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
# sum of a and b arrays
print(f"Sum of a and b is {a+b}")
# difference of a and b arrays
print(f"Difference of a and b is {a-b}")
# multiplication of a and b arrays
print(f"Multiplication of a and b is {a*b}")
# dot product of a and b arrays
print(f"Dot product of a and b is {a.dot(b)}")
# division of a and b arrays
# actually it is like a*inverse(b)
print(f"Division (a*b^-1) of a and b is {a/b}")
