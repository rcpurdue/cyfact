import math
from timeit import timeit
import numpy as np

from src import cytest as intp  # Access cytest.py
from src import cytestcomp as comp  # Access compiled library

TEST_INTEGER = 12
TEST_MATRIX = np.random.randn(TEST_INTEGER, TEST_INTEGER)
TEST_THRESHOLD = 0.5


def test(name, code, n=10000):
    """Time code execution using many repetitions"""
    result = timeit(stmt=code, globals=globals(), number=n)
    print(f"{name}: {(result / n):.8f} seconds")


if __name__ == "__main__":

    print('Factorial...')
    assert math.factorial(TEST_INTEGER) == intp.factorial(TEST_INTEGER) == comp.factorial(TEST_INTEGER)
    test('Interpreted', lambda: intp.factorial(TEST_INTEGER))
    test('Compiled   ', lambda: comp.factorial(TEST_INTEGER))
    test('Library    ', lambda: math.factorial(TEST_INTEGER))

    print('Threshold...')
    test('Interpreted', lambda: intp.threshold(TEST_MATRIX, TEST_THRESHOLD))
    test('Compiled   ', lambda: comp.threshold(TEST_MATRIX, TEST_THRESHOLD))
    test('Library    ', lambda: np.where(TEST_MATRIX > TEST_THRESHOLD, 1, 0))
