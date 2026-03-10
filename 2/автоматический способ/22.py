def f(x,y,z,w):
    return ((w or not(z)) and x and (not(y)))
tables=[(0,0,0,1),(0,1,1,1),(0,1,0,1)]
from  itertools import permutations
for i in permutations('xyzw'):
    yu=[f(**dict(zip(i,ik))) for ik in tables]
    if yu==[1,1,1]:
        print(i)