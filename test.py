import math
from timeit import timeit

from src import cyfact as intp  # Brings in cyfact.py
from src import cyfactcomp as comp  # Brings in the .so

TEST_VALUE = 12


def test(name, code, n=10000000):
    result = timeit(stmt=code, globals=globals(), number=n)
    print(f"{name}: {(result / n):.8f} seconds")


if __name__ == "__main__":
    print('Same value? ', math.factorial(TEST_VALUE)
          == intp.factorial(TEST_VALUE)
          == comp.factorial(TEST_VALUE))
    test('Interpreted', f'intp.factorial({TEST_VALUE})')
    test('Compiled   ', f'comp.factorial({TEST_VALUE})')
    test('Library    ', f'math.factorial({TEST_VALUE})')
