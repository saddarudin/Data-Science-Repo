# Write a function that calculates the sum of elements at odd indices in a list.
def odd_indices_sum(list_a):
    temp = 0
    for i in range(1, len(list_a), 2):
        temp = temp+list_a[i]
    return temp


my_list = [1, 2, 3, 1, 5, 3, 6, 21, 35, 123, 434, 22, 12, 13, 123, 23, 64, 43, 23, 42, 65]
print(odd_indices_sum(my_list))
