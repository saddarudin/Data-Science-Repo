# Create a class called Employee with attributes name, salary, and designation.
# Write a method calculate_bonus() that calculates and returns 10% of the salary as bonus.

class Employee:
    def __init__(self, name, salary, designation):
        self.name = name
        self.salary = salary
        self.designation = designation

    def calculate_bonus(self):
        return self.salary/10


e1 = Employee("Ali Asghar", 50000, "Teacher")
print(e1.calculate_bonus())
