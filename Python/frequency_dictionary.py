# Write a function that takes a list of elements as input and returns a dictionary
# with the count of each unique element in the list.

def frequency(list_a):
    my_dict = {}
    unique_list = []
    for item in list_a:
        if item not in unique_list:
            unique_list.append(item)
    for item in unique_list:
        my_dict[item] = list_a.count(item)

    return my_dict


list_one = [1, 2, 3, 1, 2, 4, 2, 4, 1, 5, 2, 6, 4, 6, 7]
dictionary_a = frequency(list_one)
print("Value: Frequency")
for key in dictionary_a:
    print(key, "    ", dictionary_a[key])

