# cyfact - Example code for intro to Cython's "pure Python" mode

NOTE: Not yet tested on Windows and Mac. Might work as-is (?)

## How to use
- Run ```compile.py``` first:
    - Uses Cython to translate cyfact.py into cyfact.c
    - Creates "cyfactcomp" shared object (our own little library)
- Then, run ```test.py```:
    - Calls interpreted (Python) version of cyfact.py's ```factorial()``` and ``threshold`
    - Calls compiled (C) version of cyfact.py's ```factorial()``` and ``threshold`
    - Calls math library's ```factorial()``` an NumPy's ```where()`` for timing comparisons

## References
- syegulalp
    - [conway-2022 (repo)](https://github.com/syegulalp/conway-2022)
    - [Video](https://www.youtube.com/watch?v=sGggkVaRMzY)
- Cython Docs
    - [(Latest) Pure Python Mode](https://cython.readthedocs.io/en/latest/src/tutorial/pure.html)
- Integer
    - From docs
        - "annotating in Pure Python with int, long, and float Python types will be interpreted as Python object types"
        - "...[Python] int [maps to] cdef object..."
    - [Cython bug comment](https://github.com/cython/cython/issues/4227)
        - "PEP 526...ambiguous Python types 'int' and 'long' are not evaluated - the 'cython.int' form must be used instead."
