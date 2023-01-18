# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False
# cython: initializedcheck=False
# cython: cdivision = True
# cython: always_allow_keywords =False
# cython: unraisable_tracebacks = False
# cython: binding = False

import cython


@cython.cfunc
def cyfact_cfunc(inp: cython.int) -> cython.int:
    ans: cython.int = 2

    for i in range(3, inp+1):
        ans = ans * i

    return ans


def cyfact(inp):
    return cyfact_cfunc(inp)
