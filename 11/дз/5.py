import math

l=19
alph=26
from math import *
i=ceil(math.log2(alph))
dopinfo=40
v_partia=i*l
for lenn in range(1,10_000):
    v_num=ceil(log2(lenn))
    v_full=ceil((v_partia+v_num)/8)+dopinfo
    if lenn *v_full<=20*2**10:

        print(lenn)