import sys

from interactive_mode import get_valid_input
from quadratic_equation_solver import calculate_roots


def main():
    if len(sys.argv) == 1:
        a = get_valid_input("a = ")
        b = get_valid_input("b = ")
        c = get_valid_input("c = ")
        print(f"Equation is: ({a}) x^2 + ({b}) x + ({c}) = 0")
        roots = calculate_roots(a, b, c)

        print_roots(roots)

    elif len(sys.argv) == 2:
        pass


def print_roots(roots):
    if len(roots) == 2:
        print(f"There are 2 roots:\nx1 = {roots[0]}\nx2 = {roots[1]}")
    elif len(roots) == 1:
        print(f"There are 1 root:\nx1 = {roots[0]}")
    else:
        print("There are 0 roots")


if __name__ == "__main__":
    main()
