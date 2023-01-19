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
    """Python factorial without Cython decorators"""
    ans = 2

    for i in range(3, inp+1):
        ans *= i

    return ans


@cython.cfunc
def cfunc_factorial(inp: cython.int) -> cython.int:
    """Cython factorial"""
    ans: cython.int = 2
    i: cython.int

    for i in range(3, inp+1):
        ans *= i

    return ans


def cython_factorial(inp):
    """Enable calls to compiled function."""
    return cfunc_factorial(inp)
