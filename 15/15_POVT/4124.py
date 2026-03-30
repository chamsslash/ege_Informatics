q=list(range(7,16))
p=list(range(6,17))
a=[]
for x in range(1,10_000):
    if (((x in p) or (x not in a)) and ((x not in q) or (x in a)))==0:
        a.append(x)
print(len(a)-1)
print(a)
