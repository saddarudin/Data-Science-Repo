"""
Write circle_calc() function that takes radius of a circle as an input from
user, and then it calculates and returns area, circumference and diameter.
You should get these values in your main program by calling circle_calc function
and then print them"""

import math


def circle_calc(radius = 1):
    """
    this method calculates and returns area, circumference and diameter of circle
    :param radius: radius of circle
    :return: area, circumference and diameter of circle
    """
    return math.pi*radius**2, 2*math.pi*radius, 2*radius


if __name__ == "__main__":
    r = 2
    area, circumference, diameter = circle_calc(2)
    print(f"Area of the circle is {area}")
    print(f"Circumference of the circle is {circumference}")
    print(f"Diameter of the circle is {diameter}")
