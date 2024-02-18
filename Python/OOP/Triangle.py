# Create a class called Triangle with attributes side1, side2, and side3.
# Write a method is_valid() that checks if the triangle is valid
# (sum of any two sides is greater than the third side).

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_valid(self):
        return (self.side1+self.side2 > self.side3
                and self.side1+self.side3 > self.side2
                and self.side2+self.side3 > self.side1)


t1 = Triangle(3, 3, 1)
print(f"Is triangle valid? {t1.is_valid()}")
