"""Our first Python source file"""

from operator import floordiv, mod

def divide_exact(n, d=10):
    return floordiv(n, d), mod(n, d)

q, r = divide_exact(2013, 10)
print('Quotient:', q)
print('Remainder:', r)

def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x
