# Write a Python program to reverse a tuple.

def reverse_tuple(tuple_a):
    new_tuple = ()
    # If I write 0 in range then it will run one less than total
    # for that reason I have written -1 in between range function
    # As we know range will run the loop (second-first) time
    for i in range(len(tuple_a)-1, -1, -1):
        new_tuple = new_tuple+(tuple_a[i], )
    return new_tuple


my_tuple = (1, 1, 2, 3, 4)
reversed_tuple = reverse_tuple(my_tuple)
print(reversed_tuple)