import numpy as np

"""
There are two types of splitting horizontal and vertical
Horizontal Splitting:
It will increase numer of columns but number of rows will remain same as actual array.
And you can split to as many arrays as number of columns not more than that.
Vertical Splitting:
It will increase number of rows but number of columns will remain same as actual array.
And you can split to as many arrays as number of rows not more tha that.

Syntax:
numpy.hsplit(array, number of arrays you want)
numpy.vsplit(array, number of arrays you want)
"""

a = np.arange(36).reshape(4, 9)
print(a)
one, two, three = np.hsplit(a, 3)
print(one)

b, c, d, e = np.vsplit(a, 4)
print(b)
