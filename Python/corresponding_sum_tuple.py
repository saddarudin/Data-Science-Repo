# Write a Python function that takes two tuples of equal length as input and
# returns a new tuple containing the element-wise sum of the input tuples.

def corresponding_element_sum(tuple_a, tuple_b):
    if len(tuple_a) == len(tuple_b):
        new_tuple = ()
        for i in range(0, len(tuple_a)):
            new_tuple = new_tuple+(tuple_a[i]+tuple_b[i],)
        return new_tuple

    else:
        print("Please provide both tuple of same length.")


tuple_one = (2, 4, 6, 5, 1)
tuple_two = (1, 0, 4, 3, 2)
print(corresponding_element_sum(tuple_one, tuple_two))
