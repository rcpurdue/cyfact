# cython: language_level=3

import cython as cy


def factorial(inp: cy.int) -> cy.int:
    """Factorial, assume greater than 2"""

    # NOTE Don't use Python integers here b/c Cython compiler would map them to objects (not C ints).
    # NOTE Cython integers ("cy.int") map to Python int objects when run in regular Python interpreter (not compiled).

    ans: cy.int = 2
    i: cy.int

    for i in range(3, inp+1):
        ans *= i

    return ans


if __name__ == "__main__":
    print(factorial(12))
