from math import *
for c in range(1,100_000):
    N=1024*2048
    i=ceil(log2(1024))
    Fpaket=N*i*c
    if Fpaket/524_288<=320:
        print(c)