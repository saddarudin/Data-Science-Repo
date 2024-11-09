# Combine two lists into a single list without using the built-in + operator.
def concatenate(list_a, list_b):
    for i in range(0, len(list_b)):
        list_a.append(list_b[i])


first_list = [1, 2, 3, 4, 5]
second_list = [6, 7, 8, 9, 10]
concatenate(first_list, second_list)
print(first_list)

