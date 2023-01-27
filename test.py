import math
from timeit import timeit

from src import cyfact as intp  # Bring in cyfact.py
from src import cyfactcomp as comp  # Bring in compiled library

TEST_VALUE = 12


def test(name, code, n=10000000):
    """Time code execution using many repetitions"""
    result = timeit(stmt=code, globals=globals(), number=n)
    print(f"{name}: {(result / n):.8f} seconds")


if __name__ == "__main__":

    # Make sure both versions of our factorial() are correct
    print('Same value? ', math.factorial(TEST_VALUE)
          == intp.factorial(TEST_VALUE)
          == comp.factorial(TEST_VALUE))

    # Compare performance
    test('Interpreted', f'intp.factorial({TEST_VALUE})')
    test('Compiled   ', f'comp.factorial({TEST_VALUE})')
    test('Library    ', f'math.factorial({TEST_VALUE})')
