import sys
import os
import glob

from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

sys.argv = ["compile.py", "build_ext", "--inplace"]

for ff in ("*.c", "*.html"):
    for f in glob.glob(ff):
        try:
            os.remove(f)
        except FileNotFoundError:
            pass

ext_modules = [
    Extension(
        "cyfact",
        ["cyfact.py"],

    )
]

os.chdir("src")

setup(name="cyfact", ext_modules=cythonize(ext_modules, annotate=True))
