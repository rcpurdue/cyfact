# cython: language_level=3

import cython as cy


def factorial(inp: cy.int) -> cy.int:
    """Factorial, assume greater than 2"""

    # NOTE Python integers not used here as Cython compiler would map them to C objects (not C ints).
    #      But, when run in Python interpreter (not compiled), "cy.int" DOES map to Python integer.

    ans: cy.int = 2
    i: cy.int

    for i in range(3, inp+1):
        ans *= i

    return ans


if __name__ == "__main__":
    print(factorial(12))
