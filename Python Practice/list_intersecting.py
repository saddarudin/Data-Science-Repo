# Write a function that takes two lists as input and returns a
# new list containing only the common elements.
def intersect(list_a, list_b):
    intersecting_list = []
    for i in list_a:
        if i in list_b:
            intersecting_list.append(i)

    return intersecting_list


list_one = [1, 2, 3, 4, 5]
list_two = [2, 1, 5, 4, 6]
new_list = intersect(list_two, list_one)
print(new_list)
