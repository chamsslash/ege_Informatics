N=1024*512
c=256
from math import ceil,log2
for n in range(1,10_000):
    i=ceil(log2(n))
    F=i*c*N
    if F/6393911<160:
        print(n)