import numpy as np
"""
There are two methods of stacking vertical stacking and horizontal stacking.
In vertical stacking other arrays rows are added at the bottom of first array.
In horizontal stacking other arrays rows are added to each row of the first arra.

Syntax:
numpy.vstack(tuple)
numpy.hstack(tuple)
It takes tuple as input in which first argument is array that is going to be stacked
with second array and second argument is second array
"""
a = np.arange(0, 6).reshape(3, 2)
b = np.arange(6, 12).reshape(3, 2)
print("Doing vertical stacking...")
print(np.vstack((a, b)))
print("Doing horizontal stacking...")
print(np.hstack((a, b)))
