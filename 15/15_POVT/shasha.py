i=list(range(9,21))
n=list(range(6,27))
f=list(range(4,39))
o=[]
for x in range(1,10_000):
    if ((((2*x) not in i) and (x in n)) <= ((x not in f)  or (x in o)))==0:
        o.append(x)
print(o[-1]-o[0])