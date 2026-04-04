from functools import lru_cache
from sys import setrecursionlimit
setrecursionlimit(1000000)
@lru_cache(maxsize=None)
def f(n):
    if n >=20:
        return (f(n-4))+4620
    if n<20:
        return 8*((g(n-12)) - 21)
@lru_cache(maxsize=None)
def g(n):
    if n >=384242:
        return (n/4 + 18)
    if n<384242:
        return  12+g(n+41)
for x in range(384242,-20,-1):
    g(x)

for y in range(1,915):
    f(y)

print(f(913))