def remove_duplication(list_a):
    unique_list = []
    for item in list_a:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


my_list = [1, 1, 1, 2, 3, 1, 3, 3, 5, 4, 5, 6, 6, 1, 1, 2, 5, 7, 5, 7, 8]
new_list = remove_duplication(my_list)
print(new_list)
