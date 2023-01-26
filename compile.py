import sys
import os
import glob
import logging

from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize


sys.argv = ["compile.py", "build_ext", "--inplace"]
logging.basicConfig(level=logging.DEBUG)

for ff in ("*.c", "*.html"):

    for f in glob.glob(ff):

        try:
            os.remove(f)
        except FileNotFoundError:
            pass

os.chdir("src")
setup(name="cyfactcomp", ext_modules=cythonize([Extension("cyfactcomp", ["cyfact.py"], )], annotate=True))
