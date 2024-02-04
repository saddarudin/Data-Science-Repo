# Write a Python function that takes a list of numbers as input and returns
# the sum of all the elements in the list.
numbers = input("Enter list of numbers: ")
num = numbers.split(",")
total=0
for i in num:
    total=total+int(i)


print(total)