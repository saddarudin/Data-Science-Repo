"""
Write a function that takes two arguments an array say 'a' and a number
say 'x' and returns the array containing the number greater than 'x'
"""
import numpy as np


def filter_array(a, x):
    """
    This function filters the number which are greater than x
    :param a: array
    :param x: any number
    :return: array
    """
    c = a>x
    return a[c]


# c in above function returns an array in of boolean values in which there is true when number is greater than x
# false otherwise  and in return statement a[c] means a will compare each of its element with each element of c if true
# then store in new array not otherwise.
ar = np.arange(15).reshape(5, 3)
b = filter_array(ar, 4)
print(b)
