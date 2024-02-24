# Create a class called Rectangle with attributes length and width.
# Write a method calculate_area() that calculates and returns the
# area of the rectangle.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length*self.width


r1 = Rectangle(5, 5)
r2 = Rectangle(2.5, 3.1)
print(r1.calculate_area())
print(r2.calculate_area())
