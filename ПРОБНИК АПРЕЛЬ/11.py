N=10+70
from math import *
i=ceil(log2(N))
res=[]
for dlina in range(1,1000):
    r=ceil(i*dlina/8)
    if (1234567*r>24*2**20):
        res.append(dlina)
print(min(res))