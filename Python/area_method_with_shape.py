# Modify area function to take third parameter shape type. It can be either "triangle" or "rectangle".
# Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def area(base, height, shape='triangle'):
    """
    This method calculates the area of the shape provided in argument
    i.e. either Triangle or Rectangle
    :param base: base of triangle or rectangle
    :param height: height of triangle or rectangle
    :param shape: either triangle or rectangle
    :return: area of the shape
    """

    if shape == 'rectangle':
        return base*height
    else:
        return 0.5*base*height


b = 2
h = 4
print(f"Area of the triangle is {area(base=b, height=h, shape='triangle')}")
print(f"Area of the rectangle is {area(base=b, height=h, shape='rectangle')}")
