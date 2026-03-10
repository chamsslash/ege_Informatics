from itertools import product, permutations


def f(x,y,z,w):
    o1= ((z<=y) == (x <= (not w))) and (x or y)
    return o1
for t in product([0,1],repeat=2):
    table=[(0,1,1,1),(1,0,1,0),(t[0],0,0,t[1])]
    if len(set(table))==3:
        for o in permutations('xyzw'):
            resh=[f(**dict(zip(o,tab))) for tab in table]
            if resh==[0,1,1]:
                print(o)