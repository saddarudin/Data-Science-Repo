# Write a Python program to count the frequency of elements in a given tuple.

def frequency(tuple_a):
    my_dict = {}
    unique_tuple = ()
    for i in tuple_a:
        if i not in unique_tuple:
            unique_tuple = unique_tuple+(i, )

    for i in unique_tuple:
        my_dict[i] = tuple_a.count(i)

    return my_dict


my_tuple = (1, 2, 4, 6, 1, 7, 2, 1, 4, 0, 0, 0, 8, 9, 7, 9, 0, 5, 6, 7, 8, 3)
print(frequency(my_tuple))
