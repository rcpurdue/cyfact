import sys
import os
import glob

from setuptools import setup, Extension
from Cython.Build import cythonize


sys.argv = ["compile.py", "build_ext", "--inplace"]

for ff in ("*.c", "*.html"):

    for f in glob.glob(ff):

        try:
            os.remove(f)
        except FileNotFoundError:
            pass

os.chdir("src")
setup(name="cytestcomp", ext_modules=cythonize([Extension("cytestcomp", ["cytest.py"], )], annotate=True))
