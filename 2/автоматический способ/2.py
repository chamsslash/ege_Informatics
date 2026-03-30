def f(x,y,w,z):
    u= ((not(x)) and ((z <= y) <= w))
    return u
from itertools import product, permutations

for i  in product([0,1], repeat=4):
    tables=[(0,i[0],1,i[1]),(1,i[2],0,1),(0,0,i[3],1)]
    if len(set(tables))==3:
        for p in permutations('xyzw'):
            ty=[f(**dict(zip(p,table))) for table in tables]
            if ty==[1,1,0]:
                print(p)