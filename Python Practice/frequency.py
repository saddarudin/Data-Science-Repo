# Write a program that counts the occurrences of each element in a
# given list and returns a dictionary with the counts.

def frequency_method(list_a):
    unique_list = []
    for item in list_a:
        if item not in unique_list:
            unique_list.append(item)
    for i in unique_list:
        print(f"Value: {i}, frequency: {list_a.count(i)}")


my_list = [1, 2, 1, 2, 3, 1, 3, 2, 3, 1, 1, 2, 3, 5, 6, 5, 6, 6, 7]
frequency_method(my_list)