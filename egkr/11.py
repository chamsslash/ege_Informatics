alph=1015+10
from math import *
i=ceil(log2(alph))
ident_v=ceil((i*289)/8)
o1=(ident_v*524288)/2**20
print(o1)
print(len(bin(2047)[2:]))