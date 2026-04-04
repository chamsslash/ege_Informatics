from itertools import product, permutations


def f(x,y,z,w):
    return (not(z) and y and x and not(w)) or (not(z) and y and not(x) and not(w)) or (z and y and x and not(w))
for i in product([1,0],repeat=7):
    tables=[(i[0],1,i[1],i[2]),(i[3],0,1,i[4]),(0,i[5],0,i[6])]
    if len(set(tables))==3:
        for ii in permutations('xyzw'):
            if ([f(**dict(zip(ii,table))) for table in tables]) == [1,1,1]:
                print(ii)