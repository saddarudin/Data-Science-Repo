# swap two variables without using third variable
a =5
b = 6
print(f"before swapping a: {a}, b:{b}")
a = a+b
b = a-b
a = a-b
print(f"after swapping a:{a}, b:{b}")