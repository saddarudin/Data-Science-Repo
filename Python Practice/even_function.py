# Write a function that takes a list of integers and returns a new list containing only the even numbers.
def even_function(num_list):
    for i in num_list:
        if i % 2 != 0:
            num_list.remove(i)


numeric_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_function(numeric_list)
print(numeric_list)
