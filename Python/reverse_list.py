# Create a program that reverses the order of elements in
# a given list without using the built-in reverse() method.
my_list = [10, 11, 12, 13, 14, 15]
for i in range(0, len(my_list)//2):
    temp = my_list[i]
    my_list[i]=my_list[len(my_list)-1-i]
    my_list[len(my_list)-1-i]=temp

print(my_list)
