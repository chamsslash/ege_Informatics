def resh(x,y,z,w):
    return ((w<=y)<=x)or not(z)
from itertools import *
for i in product([1,0],repeat=7):
    table=[(i[0],i[1],1,i[2]),  (i[3],0,i[4],i[5]), (i[6],1,0,0)]
    if len(set(table))==3:
        for u in permutations('xyzw',r=4):
            if [resh(**dict(zip(u,t)))for t in table] ==[0,0,0]:
                print(u)
