def funca(x,y,w,z):
    o1=(x or y) and not(y==z) and not(w)
    return o1
from itertools import product,permutations
for i in product([0,1],repeat=4):
    tables=[(i[0],i[1],i[2],1),(0,1,0,0),(1,0,0,i[3])]
    if len(set(tables))==3:
        for p in permutations('xyzw'):
            resh=[funca(**dict(zip(p,tab))) for tab in tables]
            if resh==[1,1,1]:
                print(p)