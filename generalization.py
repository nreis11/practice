"""Generalization
Explanation: Optimizing the code to eliminate redundency"""

from math import pi, sqrt

def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) / 2)

def sum_naturals(n):
    """Sum the first n natural numbers.

    >>> sum_naturals(5)
    15
    """

    total, k = 0, 1
    while k <= n:
        total, k = total + k, k + 1
    return total

def make_adder(n):
    """Returns a function that takes argument K and
    returns K + N.

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder
