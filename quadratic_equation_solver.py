import math


def calculate_roots(a: float, b: float, c: float):
    d = b**2 - 4.0 * a * c
    d_sqrt = math.sqrt(d)
    if d < 0:
        return []
    x1 = (-b + d_sqrt) / (2.0 * a)
    if d == 0:
        return [x1]
    else:
        x2 = (-b - d_sqrt) / (2.0 * a)
        return [x1, x2]
