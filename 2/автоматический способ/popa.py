def func(x,y,z,w):
    oi=((x<=y)==(w<=(not z)) and (w or y))
    return oi
from itertools import permutations,product
for pr in product([0,1],repeat=2):
    tables=[(1,1,1,0),(0,0,1,1),(pr[0],0,0,pr[1])]
    if len(set(tables))==3:
        for perm in permutations('xyzw'):
            sbor=[func(**dict(zip(perm,tab)))for tab in tables]
            if sbor == [0,1,1]:
                print(perm)