a=list( i/10 for i in range(30,1051))
b=list(i for i in range(2,206) if 206%i==0)
for y in range(1,10_000):
    c=[i for i in range(2,y) if y%i==0]
    if c:
        for x in range(1,10_000):
            if ((x in c)<= ((x in a) and not (x in b)))==0:
                break
        else:
            print(y)
