import math

class Point(object):
    """Represents a point in two-dimensional geometric coordinates"""

    def __init__(self, x=0, y=0):
        """Initializes the position of a new point. If no points are given,
        then the points default to the origin"""
        self.move(x, y)

    def move(self, x, y):
        """Move the point to another location"""
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate_distance(self,other_point):
        """Calculates the distance from this point to another point passed as
        a parameter. This function uses the Pythagorean theorem to calculate
        the distance."""

        return math.sqrt((self.x - other_point.x) ** 2 +
        (self.y - other_point.y) ** 2)

my_point = Point(3, 5)
