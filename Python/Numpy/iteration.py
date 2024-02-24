import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Printing rows...")
for row in a:
    print(row)
print("Printing elements...")
for row in a:
    for element in row:
        print(element)

print("Printing elements using flat...")
for element in a.flat:
    print(element)
    