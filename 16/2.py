from functools import lru_cache
from sys import setrecursionlimit

setrecursionlimit(10000)
@lru_cache(None)
def F(n):
    if n>=20:
        return F(n-4)+4620
    else:
        return 8*(G(n-12)-21)
def G(n):
    if n>=384242:
        return n/4+18
    else:
        return 12+ G(n+41)
print(F(913))