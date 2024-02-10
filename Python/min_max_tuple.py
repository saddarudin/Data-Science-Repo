# Write a Python program to find the maximum and minimum elements in a tuple of integers.
def minimum(tuple_a):
    smallest = tuple_a[0]
    for i in range(1, len(tuple_a)):
        if tuple_a[i]<smallest:
            smallest = tuple_a[i]
    return smallest


def maximum(tuple_a):
    largest = tuple_a[0]
    for i in range(1, len(tuple_a)):
        if tuple_a[i]>largest:
            largest = tuple_a[i]
    return largest


my_tuple = (1, 2, 3, 4, 5, 6, 15, 0, 5, 7, -3, 1, -2, 56, 7)
print(f"Minimum value in the given tuple is {minimum(my_tuple)}")
print(f"Maximum value in the given tuple is {maximum(my_tuple)}")
