from math import *
lencode=17
N=52
icode=ceil(log2(N))
partyV=icode*lencode
dopV=50
for numberofproducts in range(1,10_000):
    bits=ceil(log2(numberofproducts))
    F=ceil((bits+partyV)/8)+50
    if numberofproducts*F<=90 *2**10:
        print(numberofproducts)