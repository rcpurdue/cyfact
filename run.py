import time

from src.cyfact import cyfact  # , cyfact_cfunc
from fact import fact

start = time.time()
test = 12
print(cyfact(test), (time.time() - start) * 10000000)
# print(cyfact_cfunc(test), (time.time() - start) * 10000000)
print(fact(test), (time.time() - start) * 10000000)
