l=22
from math import log2,ceil
i=ceil(log2(26))
for kolvoproducts in range(1,10_000):
    v_num=ceil(log2(kolvoproducts))
    vfull=ceil((v_num+(i*l))/8)+50
    if vfull*kolvoproducts<=30 *2**10:
        print(kolvoproducts)