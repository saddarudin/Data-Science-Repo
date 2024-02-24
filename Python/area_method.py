# Write a function called calculate_area that takes base and height as an
# input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def calculate_area(base, height):
    """
    This function calculates the area of triangle
    :param base: base of triangle
    :param height: height of triangle
    :return: area of triangle
    """
    return 0.5*base*height


b = 5
h = 6
print(f"Area of triangle is {calculate_area(base=b, height=h)}")
