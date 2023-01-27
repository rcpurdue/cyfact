# cython: language_level=3

import cython as cy


def factorial(inp: cy.int) -> cy.int:
    """Factorial, assume greater than 2"""

    # NOTE 1. PEP 526 type annotations inform Cython's "pure python" mode so it can assign C types.
    #      2. Python integers not used here as Cython compiler would map them to C objects (not C ints).
    #      3. When run in Python interpreter (not compiled), "cy.int" maps to Python integer.

    ans: cy.int = 2
    i: cy.int

    for i in range(3, inp+1):
        ans *= i

    return ans


if __name__ == "__main__":
    print(factorial(12))
