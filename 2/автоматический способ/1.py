def res(x,y,z,w):
    a= ((w or not(z))and x and not(y))
    return a
from itertools import *
tables=[(0,0,0,1),(0,1,1,1),(0,1,0,1)]
# перебор перестановок пермутешнов букв
for i in permutations('xyzw'):
    o=[res(**dict(zip(i,uwu))) for uwu in tables]
    if o ==[1,1,1]:
        print(i)