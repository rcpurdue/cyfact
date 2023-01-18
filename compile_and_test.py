import time
import sys
import os
import glob
import logging

from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

import src.cyfact

sys.argv = ["compile.py", "build_ext", "--inplace"]
logging.basicConfig(level=logging.DEBUG)


# Clean up

for ff in ("*.c", "*.html"):

    for f in glob.glob(ff):

        try:
            os.remove(f)
        except FileNotFoundError:
            pass

# Compile
os.chdir("src")
setup(name="cyfact", ext_modules=cythonize([Extension("cyfact", ["cyfact.py"], )], annotate=True))

# Test
logging.info('Test results follow...')
test = 12
start = time.time()
print('Python result:', src.cyfact.python_factorial(test), 'Time:', (time.time() - start) * 1000000)
start = time.time()
print('Cython result:', src.cyfact.cython_factorial(test), 'Time:', (time.time() - start) * 1000000)
