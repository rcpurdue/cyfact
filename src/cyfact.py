# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: initializedcheck=False
# cython: cdivision = True
# cython: always_allow_keywords =False
# cython: unraisable_tracebacks = False
# cython: binding = False

import cython


def python_factorial(inp):
    """Just compiling normal Python"""
    ans = 2

    for i in range(3, inp+1):
        ans *= i

    return ans


@cython.cfunc
def cfunc_pep526_factorial(inp: int) -> int:
    """Compiled but with PEP526 type annotations"""
    ans: int = 2
    i: int

    for i in range(3, inp+1):
        ans *= i

    return ans


@cython.cfunc
def cfunc_factorial(inp: cython.int) -> cython.int:
    """Compiled with Cython types"""
    ans: cython.int = 2
    i: cython.int

    for i in range(3, inp+1):
        ans *= i

    return ans


def pep526_factorial(inp):
    """Enable calls to compiled function."""
    return cfunc_pep526_factorial(inp)


def cython_factorial(inp):
    """Enable calls to compiled function."""
    return cfunc_factorial(inp)
