l=283
from math import log2,ceil
for n in range(1,10_000):
    i=ceil(log2(n))
    ser=ceil((i*l)/8)
    if ser*65_536>15*2**20:
        print(n)
        break