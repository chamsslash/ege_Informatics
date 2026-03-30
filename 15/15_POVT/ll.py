q=list(range(20,40+1))
p=list(range(10,26))
a=[]
for x in range(1,10_000):
    if (((x in p) and (x not in q))<= (x in a))==0:
        a.append(x)
print(a)
