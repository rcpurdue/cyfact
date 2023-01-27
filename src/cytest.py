# cython: language_level=3

import cython as cy
import numpy as np


def factorial(input: cy.int) -> cy.int:
    """Factorial, assume greater than 2"""

    # NOTE 1. PEP 526 type annotations inform Cython's "pure python" mode so it can assign C types.
    #      2. Python integers not used here as Cython compiler would map them to C objects (not C ints).
    #      3. When run in Python interpreter (not compiled), "cy.int" maps to Python integer.

    output: cy.int = 2
    i: cy.int

    for i in range(3, input+1):
        output *= i

    return output


def threshold(input: np.ndarray, value: float) -> np.ndarray:
    """Convert matrix to binary"""
    output: np.ndarray = np.zeros_like(input)
    i: cy.int
    j: cy.int

    for i in range(input.shape[0]):

        for j in range(input.shape[1]):

            if input[i][j] > value:
                output[i][j] = 1

    return output


if __name__ == "__main__":
    print(factorial(12))
    print(threshold(np.random.randn(100, 100), 0.5))
