from itertools import product, permutations


def f(x,y,w,z):
    o1=((x and not(y)) and (w <=z))
    return o1
for i in product([0,1],repeat=6):
    tables=[(0,i[0],i[1],1),(0,i[2],1,1),(1,i[3],i[4],1)]
    if len(set(tables))==3:
        for p in permutations('xyzw'):
            resh=[f(**dict(zip(p,tab))) for tab in tables]
            if resh==[1,1,1]:
                print(p)
