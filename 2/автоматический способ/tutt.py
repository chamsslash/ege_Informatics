from itertools import permutations,product
def f1(x,y,z,w):
    v1=((w==z)and(y<=x))
    return  v1
def f2(x,y,z,w):
    v2=((w<=z)<=(x==y))
    return v2
for no in product([0,1],repeat=4):
    tables=[(1,no[0],1,1),(0,1,0,no[1]),(no[2],0,0,no[3])]
    if len(set(tables))==3:
        for lets in permutations('xyzw'):
            res1=[f1(**dict(zip(lets,i)))for i in tables]
            res2=[f2(**dict(zip(lets,i1)))for i1 in tables]
            if res1 == [1,1,0] and ((res2 == [0,0,0]) or (res2 == [0,1,0])):
                print(lets)