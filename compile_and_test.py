import sys
import os
import glob
import logging
import math

from timeit import timeit
from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

import src.cyfact


TEST_VALUE = 12

sys.argv = ["compile.py", "build_ext", "--inplace"]
logging.basicConfig(level=logging.DEBUG)


def interpreter_factorial(inp):
    """Python factorial function to be run in interpreter."""
    ans = 2

    for i in range(3, inp+1):
        ans *= i

    return ans


def test(name, code, n=100000):
    result = timeit(stmt=code, globals=globals(), number=n)
    print(f"{name}: {(result / n):.8f} seconds")


def clean_up():
    for ff in ("*.c", "*.html"):

        for f in glob.glob(ff):

            try:
                os.remove(f)
            except FileNotFoundError:
                pass


def compile():
    os.chdir("src")
    setup(name="cyfact", ext_modules=cythonize([Extension("cyfact", ["cyfact.py"], )], annotate=True))


clean_up()
compile()
print(interpreter_factorial(TEST_VALUE)
      == math.factorial(TEST_VALUE)
      == src.cyfact.python_factorial(TEST_VALUE)
      == src.cyfact.cython_factorial(TEST_VALUE))
test('Interpreted ', f'interpreter_factorial({TEST_VALUE})')
test('Compiled    ', f'src.cyfact.python_factorial({TEST_VALUE})')
test('Cython      ', f'src.cyfact.cython_factorial({TEST_VALUE})')
test('Library     ', f'math.factorial({TEST_VALUE})')
