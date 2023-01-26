# cyfact - Example code (factorial calculation) for learning Cythong

References
- syegulalp
    - [conway-2022 (repo)](https://github.com/syegulalp/conway-2022)
    - [Video](https://www.youtube.com/watch?v=sGggkVaRMzY)
- Cython Docs
    - [(Latest) Pure Python Mode](https://cython.readthedocs.io/en/latest/src/tutorial/pure.html)
- Integer
    - Docs: "...[Python] int [maps to] cdef object..."
    - [Cython bug comment](https://github.com/cython/cython/issues/4227)
        - "PEP 526...ambiguous Python types 'int' and 'long' are not evaluated - the 'cython.int' form must be used instead."
