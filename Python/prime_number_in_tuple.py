# Write a Python function that takes a tuple of integers as input and returns
# a new tuple containing only the prime numbers from the input tuple.

def prime(num):
    if num<2:
        return False
    for i in range(2, (num//2)+1):
        if num % i == 0:
            return False
    return True


def prime_tuple(tuple_a):
    new_tuple = ()
    for value in tuple_a:
        if prime(value):
            new_tuple = new_tuple+(value,)
    return new_tuple


my_tuple = (1, 2, 5, 7, 45, 67, 89, 0, 12, 3, 4, 5, 6, 8, 9, 10, 13, 11, 12)
print(prime_tuple(my_tuple))
