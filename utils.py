# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

from math import *

def fact(n):
    if n < 0:
        raise ValueError
    result = 1
    for i in range(1, n+1):
        result *= i

    return result
    

def roots(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        return ()
    elif discriminant == 0:
        return ( (-b + sqrt(discriminant)) / (2 * a) )
    else:
        return ( (-b + sqrt(discriminant)) / (2 * a), (-b - sqrt(discriminant)) / (2 * a) )

def integrate(function, lower, upper):
    steps = 100
    h = (upper - lower) / steps
    x = lower

    integral = 0

    for i in range(steps + 1):
        if i == 0 or i == steps:
            integral += eval(function, {}, {'x': x})
        elif i % 2 == 0:
            integral += 2 * eval(function, {}, {'x': x})
        else:
            integral += 4 * eval(function, {}, {'x': x})

        x += h

    integral *= h/3

    return integral

if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
