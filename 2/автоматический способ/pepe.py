def elpepe(x,y,z,w):
    o=(not(x<=w) or (x==z) or y)
    return o
from itertools import permutations,product
for i in product([0,1],repeat=6):
    tables=[(0,1,i[0],1),(i[1],i[2],1,1),(i[3],i[4],1,i[5])]
    if len(set(tables))==3:
        for j in permutations('xyzw'):
            resh=[elpepe(**dict(zip(j,tab)))for tab in tables]
            if resh==[0,0,0]:
                print(j)