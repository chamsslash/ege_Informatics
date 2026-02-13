N=52
from math import ceil,log2
ipart=ceil(log2(N))
vpart=21*ipart
for numberofproducts in range(1,10000):
    bits=log2(numberofproducts)
    full=ceil((vpart+bits)/8)+60
    if numberofproducts*full<80*2**10:
        print(numberofproducts)