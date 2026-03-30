a=list(range(3,55))
b=[i for i in range(2,137) if 137%i==0 ]
for y in range(10_000,1,-1):
    c=[i for i in range(2,y) if y%i==0]
    if c:
        for x in range(1,10000):
            if ((x in c)<= ((x in a) and (x not in b)))==0:
                break
        else:
            print(y)