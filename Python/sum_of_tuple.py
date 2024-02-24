# Write a Python function that takes a tuple of numbers as input
# and returns the sum of all the elements in the tuple.

def sum_of_tuple(tuple_a):
    total = 0
    for i in tuple_a:
        total = total+i

    return total


my_tuple = (2, 2, 3)
print(sum_of_tuple(my_tuple))
