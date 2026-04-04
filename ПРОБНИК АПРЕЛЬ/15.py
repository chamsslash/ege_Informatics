a=list(range(3,61))
b=[i for i in range(2,177) if 177%i==0]
res=[]
for y in range(1,10_000):
    c = [i for i in range(2, y) if y % i == 0]
    if len(c)!=0:
        for x in range(10000):
            if ((x in c ) <= ((x in a) and not(x in b)))==0:
                break
        else:
            res.append(y)

print(max(res))