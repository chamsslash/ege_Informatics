a=list(range(3,61))
b=[i for i in range(2,177) if 177%i==0]
for y in range(2,10_0000):
    c=[i for i in range(2,y) if y%i==0]
    if c:
        for x in range(1,10_000):
            if ((x in c) <= ((x in a) and (x not in b)))==0:
                break
        else:
            print(y)